# CLI Todo Manager

A command-line todo application built in Python that supports basic CRUD operations, JSON persistence, input validation, and pytest-based testing.

## Features

- Add a new task
- List all tasks
- Mark a task as completed
- Delete a task
- Save tasks to `tasks.json`
- Load saved tasks when the program starts
- Validate empty task titles
- Handle invalid task ID input safely

## Technologies Used

- Python
- JSON
- Git
- GitHub
- pytest

## How to Run

1. Open the project folder in VS Code or your terminal
2. Navigate to the project directory:
   ```bash
   cd projects/cli-todo-manager
   ```
3. Run the app:
   ```bash
   python todo.py
   ```

## How to Run Tests

From the project folder, run:

```bash
pytest test_todo.py
```

Or from the repository root, run:

```bash
pytest projects/cli-todo-manager/test_todo.py
```

## Example Menu

```text
Todo Menu
1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Exit
```

## What I Practiced

While building this project, I practiced:

- Functions
- Lists and dictionaries
- JSON file handling
- CRUD operations
- Input validation
- Error handling with `try`/`except`
- Writing automated tests with pytest
- Refactoring code into smaller handler functions
- Git and GitHub workflow

## Future Improvements

- Add task priorities
- Add due dates
- Improve task editing
- Add more test coverage for handler-level behavior