# Sample Data Format

The gesture recognition lab expects IMU (Inertial Measurement Unit) data in CSV format.

## File Structure

Each CSV file should contain acceleration data with the following columns:
- `X-acc`: Acceleration in the X-axis
- `Y-acc`: Acceleration in the Y-axis
- `Z-acc`: Acceleration in the Z-axis
- `label`: The gesture label (e.g., "idle", "wave", "swipe", etc.)

## Format Specifications

- **Separator**: Semicolon (`;`)
- **Samples per gesture**: 100 rows (representing 2 seconds of data)
- **Header**: First row should contain column names

## Example Data Structure

```
X-acc;Y-acc;Z-acc;label
-57;7;4154;idle
-61;9;4147;idle
-58;29;4153;idle
-61;14;4156;idle
-58;7;4151;idle
... (195 more rows)
-57;7;4154;idle
-61;9;4147;idle
-58;29;4153;idle
-61;14;4156;idle
-58;7;4151;idle
-45;120;4200;wave
-42;135;4215;wave
... (100 rows total for this gesture)
```

## Important Notes

1. Each gesture consists of **exactly 100 consecutive rows**
2. All 100 rows for a single gesture should have the **same label**
3. The header row (`X-acc;Y-acc;Z-acc;label`) appears at the start of the file
4. Multiple gestures are stored sequentially in the same file

## Placing Your Data

Place your CSV files in the `data/` directory with a descriptive name, such as:
- `data/gestures.csv`
- `data/training_data.csv`

Then update the notebook to load from the correct file path.
