# Gradebook Reporter

A Python project that reads grade data from a CSV file, converts the data into a usable Python structure, and generates summary statistics.

## Purpose

This project was built to practice structured file handling and pure-function testing. It reinforces the idea that data should be cleaned at the input boundary so later logic can stay simple.

## Features

- Load grade data from `grades.csv`
- Read rows using `csv.DictReader`
- Convert score values from strings to integers
- Summarize grade data
- Handle empty input safely
- Test summary logic with pytest

## Summary data produced

The program computes:

- Total students
- Average score
- Highest score
- Lowest score
- Passing count
- Failing count

## Concepts practiced

- CSV file handling
- `csv.DictReader`
- Type conversion with `int(...)`
- Pure functions
- Edge-case handling
- Pytest tests
- Separation of I/O from logic

## File structure

Typical files:

- `main.py`
- `grades.csv`
- `test_summary.py`

## How to run

Run tests:

```bash
python -m pytest -v
```

Run the program:

```bash
python main.py
```

## Why this project matters

This project builds a direct bridge from Python basics into backend-style data processing. It shows how to transform raw input into clean internal data, then summarize it with predictable, testable logic.