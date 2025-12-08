#!/usr/bin/env python3
"""
Serial Data Capture Script for Gesture Recognition Lab

Captures accelerometer data from firmware using the serial protocol.
Python handles all user interaction while the device provides clean data.

Usage:
    uv run python capture_serial_data.py [--port PORT] [--output FILE] [--list-ports]
"""

import argparse
import sys
import time
from pathlib import Path

import serial
import serial.tools.list_ports


def list_available_ports():
    """List all available serial ports."""
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports found.")
        return []

    print("\nAvailable serial ports:")
    print("-" * 60)
    for port in ports:
        print(f"  {port.device}")
        print(f"    Description: {port.description}")
        print()

    return [port.device for port in ports]


def find_device_port():
    """Attempt to auto-detect the device port."""
    ports = serial.tools.list_ports.comports()

    for port in ports:
        desc = port.description.lower()
        if any(pattern in desc for pattern in ['usb', 'serial', 'acm', 'gd32', 'cdc']):
            return port.device

    if ports:
        return ports[0].device

    return None


class LineReader:
    """Buffered line reader for responsive serial reading."""

    def __init__(self, ser):
        self.ser = ser
        self.buffer = ""

    def read_line(self, timeout=None):
        """Read a line, returning immediately if data available."""
        start = time.time()
        while True:
            # Check if we have a complete line in buffer
            if '\n' in self.buffer:
                line, self.buffer = self.buffer.split('\n', 1)
                return line.rstrip('\r')

            # Read any available bytes
            available = self.ser.in_waiting
            if available > 0:
                data = self.ser.read(available)
                self.buffer += data.decode('utf-8', errors='replace')
            else:
                # Small sleep to avoid busy loop
                time.sleep(0.001)

            # Check timeout
            if timeout and (time.time() - start) > timeout:
                return None


def parse_config(reader):
    """Parse the configuration block from device."""
    config = {}
    while True:
        line = reader.read_line(timeout=5)
        if line is None:
            break
        if line == "<<<CONFIG_END>>>":
            break
        if ':' in line:
            key, value = line.split(':', 1)
            config[key] = value

    # Parse values
    config['gestures'] = config.get('gestures', '').split(',')
    config['repetitions'] = int(config.get('repetitions', 5))
    config['samples'] = int(config.get('samples', 100))
    config['header'] = config.get('header', 'X-acc;Y-acc;Z-acc;label')

    return config


def wait_for_marker(reader, marker, timeout=30, debug=False):
    """Wait for a specific marker from the device."""
    start = time.time()
    while True:
        remaining = timeout - (time.time() - start)
        if remaining <= 0:
            raise TimeoutError(f"Timeout waiting for {marker}")

        line = reader.read_line(timeout=remaining)
        if line is not None:
            if debug:
                print(f"  [DEBUG] Received: {repr(line)}")
            if line == marker:
                return True


def strip_sequence_field(line):
    """Remove sequence field from line: 'seq;x;y;z;label' -> 'x;y;z;label'"""
    parts = line.split(';')
    if len(parts) == 5:
        # Format: seq;x;y;z;label -> x;y;z;label
        return ';'.join(parts[1:])
    return line  # Return as-is if format unexpected


def collect_repetition_data(reader, ser, rep_num, expected_samples, debug=False, max_retries=3):
    """Collect data for one repetition with ACK/NACK retry."""
    for attempt in range(max_retries):
        if attempt > 0 and debug:
            print(f"    [DEBUG] Retransmission attempt {attempt + 1}/{max_retries} for rep {rep_num}")

        # Wait for DATA marker
        wait_for_marker(reader, "<<<DATA>>>", debug=debug)

        # Collect data lines
        raw_lines = []
        while True:
            line = reader.read_line(timeout=10)
            if line is None:
                if debug:
                    print(f"    [DEBUG] Timeout while reading data at line {len(raw_lines)}")
                break
            if line == "<<<DATA_END>>>":
                break
            if line:
                raw_lines.append(line)

        # Wait for COUNT marker
        count_line = reader.read_line(timeout=5)
        if count_line and count_line.startswith("<<<COUNT:"):
            reported_count = int(count_line[9:-3])  # Extract number from <<<COUNT:N>>>
        else:
            reported_count = -1
            if debug:
                print(f"    [DEBUG] Missing or invalid COUNT marker: {repr(count_line)}")

        # Verify data
        actual_count = len(raw_lines)
        valid = (actual_count == expected_samples and actual_count == reported_count)

        if debug:
            status = "OK" if valid else "MISMATCH"
            print(f"    [DEBUG] Rep {rep_num} attempt {attempt + 1}: received={actual_count}, reported={reported_count}, expected={expected_samples} [{status}]")
            if raw_lines and len(raw_lines) > 0:
                print(f"    [DEBUG] First line: {raw_lines[0]}")
                print(f"    [DEBUG] Last line:  {raw_lines[-1] if raw_lines else 'N/A'}")

        if valid:
            # Send ACK
            ser.write(b'ACK\n')
            ser.flush()
            if debug:
                print(f"    [DEBUG] Sent ACK")
            # Strip sequence numbers before returning
            return [strip_sequence_field(line) for line in raw_lines]
        else:
            if attempt < max_retries - 1:
                print(f"    Retry {attempt + 1}: got {actual_count}/{expected_samples} samples, requesting resend...")
                ser.write(b'NACK\n')
                ser.flush()
                if debug:
                    print(f"    [DEBUG] Sent NACK, waiting for retransmission...")
            else:
                print(f"    Warning: Failed after {max_retries} attempts, using partial data ({actual_count} samples)")
                ser.write(b'ACK\n')  # Accept anyway to continue
                ser.flush()
                # Strip sequence numbers before returning
                return [strip_sequence_field(line) for line in raw_lines]

    return []


def collect_gesture_data(reader, ser, gesture_name, gesture_index, total_gestures, config, output_file, debug=False):
    """Collect data for one gesture with per-repetition ACK, writing to file after each rep."""
    repetitions = config['repetitions']
    samples_per_rep = config['samples']

    # Wait for READY signal
    wait_for_marker(reader, "<<<READY>>>", debug=debug)

    # Show UI
    print()
    print(f"=== Prepare for gesture: {gesture_name} ({gesture_index + 1}/{total_gestures}) ===")
    print(f"    {repetitions} repetitions, {samples_per_rep} samples each")
    print()
    input("Press ENTER when ready...")

    # Send START command
    ser.write(b'\n')
    ser.flush()
    print("Collecting data...")

    # Collect each repetition
    total_samples = 0
    for rep in range(1, repetitions + 1):
        # Wait for REP marker
        rep_marker = f"<<<REP:{rep}>>>"
        wait_for_marker(reader, rep_marker, debug=debug)

        # Collect this repetition's data
        rep_data = collect_repetition_data(reader, ser, rep, samples_per_rep, debug=debug)

        # Write immediately to file (append mode)
        with open(output_file, 'a', encoding='utf-8') as f:
            for line in rep_data:
                f.write(line + '\n')

        total_samples += len(rep_data)
        print(f"  Repetition {rep}/{repetitions} complete ({len(rep_data)} samples, written to file)")

    # Wait for GESTURE_DONE
    wait_for_marker(reader, "<<<GESTURE_DONE>>>", debug=debug)

    print(f"Completed gesture: {gesture_name} ({total_samples} samples)")

    return total_samples


def run_capture(port, output_file, debug=False):
    """Run the data capture session."""
    print(f"Connecting to {port}...")
    print(f"Output file: {output_file}")
    print()

    try:
        ser = serial.Serial(
            port=port,
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=0  # Non-blocking
        )
    except serial.SerialException as e:
        print(f"Error opening port: {e}")
        return False

    # Create buffered reader
    reader = LineReader(ser)

    try:
        print("Waiting for device...")

        # Wait for CONFIG marker
        wait_for_marker(reader, "<<<CONFIG>>>", timeout=60, debug=debug)

        # Parse configuration
        config = parse_config(reader)

        print()
        print("=" * 60)
        print("Device Configuration:")
        print(f"  Gestures: {', '.join(config['gestures'])}")
        print(f"  Repetitions per gesture: {config['repetitions']}")
        print(f"  Samples per repetition: {config['samples']}")
        total_samples = len(config['gestures']) * config['repetitions'] * config['samples']
        print(f"  Total samples: {total_samples}")
        print("=" * 60)

        # Prepare output file - write header
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Strip seq from header if present
        header = strip_sequence_field(config['header'])

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(header + '\n')

        print(f"\nWriting data to: {output_file}")

        # Collect data for each gesture (writes to file after each repetition)
        total_samples = 0
        gestures = config['gestures']

        for i, gesture in enumerate(gestures):
            samples = collect_gesture_data(reader, ser, gesture, i, len(gestures), config, output_file, debug=debug)
            total_samples += samples

        # Wait for DONE
        wait_for_marker(reader, "<<<DONE>>>")

        print()
        print("=" * 60)
        print("Collection complete!")
        print("=" * 60)
        print()
        print(f"Saved {total_samples} samples to {output_file}")

        # Summary by gesture (expected counts)
        print()
        print("Summary:")
        samples_per_gesture = config['repetitions'] * config['samples']
        for gesture in gestures:
            print(f"  {gesture}: {samples_per_gesture} samples")

        return True

    except TimeoutError as e:
        print(f"\nError: {e}")
        print("Make sure the device is connected and reset it to start fresh.")
        return False

    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return False

    finally:
        ser.close()


def main():
    parser = argparse.ArgumentParser(
        description="Capture gesture data from serial device",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run python capture_serial_data.py --list-ports
  uv run python capture_serial_data.py --port /dev/cu.usbmodem1401
  uv run python capture_serial_data.py --auto --output data/my_gestures.csv
        """
    )

    parser.add_argument('--port', '-p', type=str, help='Serial port')
    parser.add_argument('--output', '-o', type=str, default='data/TDATA_serial.csv',
                        help='Output CSV file (default: data/TDATA_serial.csv)')
    parser.add_argument('--list-ports', '-l', action='store_true', help='List available ports')
    parser.add_argument('--auto', '-a', action='store_true', help='Auto-detect port')
    parser.add_argument('--debug', '-d', action='store_true', help='Show debug output')

    args = parser.parse_args()

    if args.list_ports:
        list_available_ports()
        sys.exit(0)

    if args.auto:
        port = find_device_port()
        if not port:
            print("Error: Could not auto-detect device")
            print("Use --list-ports to see available ports")
            sys.exit(1)
        print(f"Auto-detected port: {port}")
    else:
        port = args.port

    if not port:
        print("Error: No port specified. Use --port or --auto")
        sys.exit(1)

    success = run_capture(port, args.output, debug=args.debug)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
