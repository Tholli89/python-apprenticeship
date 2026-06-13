import main


def test_mixed_scores():
    rows = [
        {"name": "Alice", "subject": "Math", "score": 88},
        {"name": "Bob", "subject": "Math", "score": 75},
        {"name": "Cara", "subject": "Math", "score": 92},
        {"name": "Dan", "subject": "Math", "score": 59},
    ]

    summary = main.summarize_grades(rows)

    assert summary["total_students"] == 4
    assert summary["average_score"] == 78.5
    assert summary["highest_score"] == 92
    assert summary["lowest_score"] == 59
    assert summary["passing"] == 3
    assert summary["failing"] == 1


def test_all_passing():
    rows = [
        {"name": "Alice", "subject": "Math", "score": 60},
        {"name": "Bob", "subject": "Math", "score": 70},
        {"name": "Cara", "subject": "Math", "score": 90},
    ]

    summary = main.summarize_grades(rows)

    assert summary["total_students"] == 3
    assert summary["average_score"] == 73.33
    assert summary["highest_score"] == 90
    assert summary["lowest_score"] == 60
    assert summary["passing"] == 3
    assert summary["failing"] == 0


def test_empty_rows():
    rows = []

    summary = main.summarize_grades(rows)

    assert summary["total_students"] == 0
    assert summary["average_score"] == 0.0
    assert summary["highest_score"] is None
    assert summary["lowest_score"] is None
    assert summary["passing"] == 0
    assert summary["failing"] == 0