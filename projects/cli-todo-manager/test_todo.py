import todo

def test_add_task(monkeypatch):
    monkeypatch.setattr(todo, "save_tasks", lambda tasks: None)

    tasks = []

    todo.add_task(tasks, "Study pytest")

    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Study pytest"
    assert tasks[0]["completed"] is False

def test_complete_task_success(monkeypatch):
    monkeypatch.setattr(todo, "save_tasks", lambda tasks: None)

    tasks = [
        {
            "id": 1,
            "title": "Study pytest",
            "completed": False
        }
    ]

    result = todo.complete_task(tasks, 1)

    assert result is True
    assert tasks[0]["completed"] is True

def test_complete_task_failure(monkeypatch):
    monkeypatch.setattr(todo, "save_tasks", lambda tasks: None)

    tasks = [
        {
            "id": 1,
            "title": "Study pytest",
            "completed": False
        }
    ]

    result = todo.complete_task(tasks, 999)

    assert result is False
    assert tasks[0]["completed"] is False

def test_save_and_load_tasks(tmp_path, monkeypatch):
    temp_file = tmp_path / "test_tasks.json"
    monkeypatch.setattr(todo, "TASKS_FILE", str(temp_file))

    tasks = [
        {"id": 1, "title": "Study Python", "completed": False},
        {"id": 2, "title": "Review Git", "completed": True}
    ]

    todo.save_tasks(tasks)
    loaded_tasks = todo.load_tasks()

    assert loaded_tasks == tasks