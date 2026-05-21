import json

def load_tasks_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_tasks(tasks):
    total = 0
    completed = 0
    incomplete = 0

    for task in tasks:
        total = total + 1

        if task["completed"] == True:
            completed = completed + 1
        else:
            incomplete = incomplete + 1

    if total == 0:
        completion_rate = 0.0
    else:
        completion_rate = round((completed / total) * 100, 2)

    summary = {
        "total":total,
        "completed":completed,
        "incomplete":incomplete,
        "completion_rate":completion_rate
        }
    
    return summary

def print_report(summary):
    print(f"total = {summary["total"]} \ncompleted = {summary["completed"]} \nincomplete = {summary["incomplete"]} \ncompletion_rate = {summary["completion_rate"]}")


def main():
    tasks = load_tasks_from_json("analytics.json")
    summary = summarize_tasks(tasks)
    print_report(summary)


if __name__ == "__main__":
    main()