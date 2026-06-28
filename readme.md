# Python Apprenticeship

This repository documents a structured software engineering apprenticeship focused on rebuilding Python, computer science fundamentals, data structures and algorithms, testing habits, Git/GitHub workflow, and early backend development from first principles.

The work in this repository is intentionally cumulative. Each project or exercise is designed to reinforce previous concepts while introducing a small amount of new complexity. The emphasis is on mastery, not speed.

## Current focus areas

This repository currently reflects practice and progress in:

- Python fundamentals
- Functions and modular program structure
- Lists and dictionaries
- File handling with JSON and CSV
- Testing with pytest
- Git and GitHub workflow
- HTTP requests with `requests`
- FastAPI basics
- Data structures and algorithms in Python

## Repository structure

### `projects/`
Contains the mini-projects built during the apprenticeship. These are practical exercises that connect programming fundamentals to job-relevant backend patterns.

Current documented projects include:

- `cli-todo-manager`
- `gradebook-reporter`
- `product-api-reporter`

### `DSA/`
Contains data structures and algorithms practice in Python.

Current topics include:

- Stack
- Queue
- Linear scan algorithms
- Array-based practice problems
- Singly linked list

## Learning approach

The repository is built around a few repeated principles:

1. Start with a small, clear problem.
2. Solve it with simple, readable Python.
3. Write tests for normal and edge cases.
4. Refactor only after the logic works.
5. Build the next exercise on top of the last one.

## Tools and technologies used so far

- Python
- pytest
- requests
- FastAPI
- Uvicorn
- Git / GitHub

## Why this repository exists

This is not just a storage place for random scripts. It is meant to show deliberate skill-building over time. The repository is intended to become evidence of:

- increasing technical depth
- better code organization
- stronger testing habits
- growing backend readiness
- improved CS fundamentals

## Running code

Different folders have their own entry points and tests.

Examples:

### Run project tests

```bash
cd projects/gradebook-reporter
python -m pytest -v
```

### Run a project

```bash
cd projects/product-api-reporter
python main.py
```

### Run the FastAPI app

```bash
cd projects/product-api-reporter
python -m uvicorn api:app --reload
```

### Run DSA tests

```bash
cd DSA
python -m pytest -v
```

## Current apprenticeship stage

The current stage of the apprenticeship has focused on rebuilding Python and CS confidence through repetition, testing, and progressively harder problems. The next stages will continue expanding backend development skill, deeper Python fluency, and stronger problem-solving ability.