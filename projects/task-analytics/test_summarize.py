import summarize

def test_mixed_tasks():
    tasks = [
    {"id": 1, "title": "Finish README", "completed": True, "priority": "high", "category": "portfolio"},
    {"id": 2, "title": "Practice Python", "completed": False, "priority": "medium", "category": "study"},
    {"id": 3, "title": "Write tests", "completed": True, "priority": "high", "category": "portfolio"}
    ]

    summary = summarize.summarize_tasks(tasks)
    assert summary["total"] == 3
    assert summary["completed"] == 2
    assert summary["incomplete"] == 1
    assert summary["completion_rate"] == 66.67

def test_completed_tasks():
    tasks = [
        {"id": 1, "title": "Task 1", "completed": True, "priority": "high", "category": "work"},
        {"id": 2, "title": "Task 2", "completed": True, "priority": "low", "category": "home"},
    ]

    summary = summarize.summarize_tasks(tasks)
    assert summary["total"] == 2
    assert summary["completed"] == 2
    assert summary["incomplete"] == 0
    assert summary["completion_rate"] == 100.0

def test_empty_tasks():
    tasks = []

    summary = summarize.summarize_tasks(tasks)

    assert summary["total"] == 0
    assert summary["completed"] == 0
    assert summary["incomplete"] == 0
    assert summary["completion_rate"] == 0.0

def test_all_incomplete():
    tasks = [
    {"id": 1, "title": "Finish README", "completed": False, "priority": "high", "category": "portfolio"},
    {"id": 2, "title": "Practice Python", "completed": False, "priority": "medium", "category": "study"},
    {"id": 3, "title": "Write tests", "completed": False, "priority": "high", "category": "portfolio"}
    ]

    summary = summarize.summarize_tasks(tasks)

    assert summary["total"] == 3
    assert summary["completed"] == 0
    assert summary["incomplete"] == 3
    assert summary["completion_rate"] == 0.0