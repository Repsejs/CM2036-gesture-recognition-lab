# Gesture Recognition Lab

A hands-on machine learning lab for bachelor students to learn practical ML workflows using TensorFlow and IMU sensor data.

## Overview

This lab guides students through a complete machine learning pipeline:
- Data collection and loading
- Data cleaning and exploration
- Preprocessing and normalization
- Data Augmentation
- Train/test splitting
- Neural network training
- Model validation and evaluation

Students will build a gesture recognition model that classifies movements based on accelerometer data (X, Y, Z acceleration values).

## Prerequisites

- Basic Python knowledge
- [uv](https://docs.astral.sh/uv/) package manager installed
- No deep mathematical background required - this is a practical, hands-on lab!

## Quick Start

### 1. Install uv (if not already installed)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone or Download This Repository

```bash
cd gesture-recognition-lab
```

### 3. Sync Dependencies

The project uses `uv` to manage all dependencies. Simply run:

```bash
uv sync
```

This will:
- Create a virtual environment in `.venv`
- Install Python 3.12
- Install all required packages (TensorFlow, NumPy, Pandas, etc.)

### 4. Prepare Your Data

Place your IMU data CSV file in the `data/` directory. See `data/sample_data_format.md` for the expected format.

### 5. Launch Jupyter (Optional, if you dont want to use an IDE)

```bash
uv run jupyter lab
```

Or if you prefer Jupyter Notebook:

```bash
uv run jupyter notebook
```

### 6. Open the Lab Notebook

Open `gesture_recognition_lab.ipynb` and follow the step-by-step instructions!

### 7. Fill Out the Answer Sheet

As you work through the lab, fill in `answers.py` with your answers to the questions from each step. Run it to check your understanding:

```bash
uv run python answers.py
```

This will verify your answers without showing you the correct ones. You must complete the answer sheet as part of the lab.

## Project Structure

```
gesture-recognition-lab/
├── README.md                      # This file
├── pyproject.toml                 # Project dependencies
├── .python-version                # Python version (3.12)
├── uv.lock                        # Locked dependencies
├── gesture_recognition_lab.ipynb  # Lab notebook with exercises
├── answers.py                     # Answer sheet (required)
└── data/
    └── sample_data_format.md      # Data format specification
```

## Data Format

Your CSV file should have this structure:

```
X-acc;Y-acc;Z-acc;label
-57;7;4154;idle
-61;9;4147;idle
...
```

- **Separator**: Semicolon (`;`)
- **Samples per gesture**: 200 rows (2 seconds of data sampled at 100 Hz)
- **Columns**: X-acc, Y-acc, Z-acc, label

See `data/sample_data_format.md` for complete details.

## Learning Objectives

By completing this lab, students will:

1. Understand the full ML workflow from data to deployment
2. Learn practical data preprocessing techniques
3. Gain hands-on experience with TensorFlow/Keras
4. Understand train/test splitting and validation
5. Learn to evaluate model performance
6. Experiment with neural network architectures

## Troubleshooting

### Virtual environment not activating

The notebook runs in the uv-managed environment automatically. Just use `uv run jupyter lab`.

### Import errors

Make sure you've run `uv sync` to install all dependencies.

### TensorFlow compatibility issues

This project uses Python 3.12 and TensorFlow 2.20+, which should work on most platforms. If you encounter issues, check the uv lock file or try `uv sync --reinstall`.

### Jupyter kernel not found

Run:
```bash
uv run python -m ipykernel install --user --name=gesture-recognition-lab
```

## Cross-Platform Compatibility

This lab uses `uv` to ensure consistent behavior across:
- macOS (Intel and Apple Silicon)
- Linux
- Windows

All dependencies are locked in `uv.lock` for reproducibility.

## Support

If you encounter issues:
1. Make sure `uv` is up to date: `uv self update`
2. Try removing `.venv` and running `uv sync` again
3. Check that your data file matches the expected format

## License

This lab is designed for educational purposes.
