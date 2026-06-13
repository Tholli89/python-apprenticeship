def load_grades_from_csv(path):
    pass

def summarize_grades(rows):
    total_students = 0
    total_score = 0
    passing = 0
    failing = 0
    highest_score = None
    lowest_score = None

    for row in rows:
        score = row["score"]
        total_students = total_students + 1
        total_score = total_score + score

        if score >= 60:
            passing = passing + 1
        else:
            failing = failing + 1

        if highest_score is None or score > highest_score:
            highest_score = score

        if lowest_score is None or score < lowest_score:
            lowest_score = score

    if total_students == 0:
        average_score = 0.0
    else:
        average_score = round(total_score / total_students, 2)

    summary = {
        "total_students": total_students,
        "average_score": average_score,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "passing": passing,
        "failing": failing,
    }

    return summary

def print_report(summary):
    print(f"total_students={summary["total_students"]} \naverage_score={summary["average_score"]} \nhighest_score={summary["highest_score"]} \nlowest_score={summary["lowest_score"]} \npassing={summary["total_passing"]} \nfailing={summary["total_failing"]}")

def main():
    load_grades_from_csv("grades.csv")
    summarize_grades(rows)
    print_report(summary)

if __name__ == "__main__":
    main()