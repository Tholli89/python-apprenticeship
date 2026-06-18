# Python Apprenticeship Projects

This folder contains the mini-projects built during the software engineering apprenticeship. The projects are intentionally small, focused, and cumulative. Each one is designed to reinforce core Python fundamentals, structured data handling, testing, debugging, and early backend development patterns.

## Purpose

The goal of this folder is to document progress through repeated practice on related problems. These projects are not random exercises. They build on each other so the same core ideas become more natural over time:

- Lists and dictionaries
- Functions and separation of concerns
- File handling with JSON and CSV
- Pure logic functions
- Pytest-based testing
- External API calls with `requests`
- Introductory FastAPI endpoints

## Projects

### 1. `cli-todo-manager`
A command-line todo manager used to practice basic Python program structure, task storage, and separating logic from user interaction.

**Concepts practiced:**
- Variables, conditionals, loops
- Functions
- Lists and dictionaries
- Command-line style interaction
- Refactoring logic into cleaner functions

### 2. `gradebook-reporter`
A CSV-based reporting project that loads grade data, converts string values at the file boundary, and summarizes student performance.

**Concepts practiced:**
- `csv.DictReader`
- Type conversion with `int(...)`
- Summarizing structured records
- Edge-case handling for empty input
- Pytest tests for pure logic functions

### 3. `product-api-reporter`
A project that fetches product data from an external API, summarizes the data, and exposes the results through a FastAPI endpoint.

**Concepts practiced:**
- HTTP requests with `requests`
- Parsing JSON responses
- Normalizing API data into a clean internal structure
- Reusing tested summary logic
- Running a local FastAPI app with Uvicorn
- Returning JSON from an API endpoint

## Recommended folder habits

As more projects are added, each project folder should include:

- Source code files
- Tests
- A project-specific `README.md`
- Clear commit history
- Small, focused scope

## Suggested workflow

1. Write the pure logic first.
2. Add tests for normal and edge cases.
3. Add file or API input/output after the logic is stable.
4. Refactor only after the code works.
5. Save the project with a meaningful commit message.

## How to use this folder

From the root of the apprenticeship folder, enter a project directory and run its tests or program.

Examples:

```bash
cd projects/gradebook-reporter
python -m pytest -v
python main.py
```

```bash
cd projects/product-api-reporter
python -m pytest -v
python main.py
python -m uvicorn api:app --reload
```

## Why these projects matter

These projects are early portfolio evidence of practical skill growth. They show repeated use of core backend-friendly patterns rather than one-off tutorial copying. The emphasis is on correctness, clarity, testability, and progressive skill-building.