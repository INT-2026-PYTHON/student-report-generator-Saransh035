"""gradebook.reports — build a printable report from grade records."""

from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students
)
def format_report(records: list[dict]) -> str:

    report = "Grade Report\n"
    report += "============\n\n"

    report += f"Total records: {len(records)}\n\n"

    report += "Subjects:\n"
    for subject in sorted(subjects_offered(records)):
        report += f"{subject}\n"

    report += "\nAverage Scores:\n"

    averages = average_per_student(records)

    for name in sorted(averages):
        report += f"{name}: {averages[name]}\n"

    name, avg = top_scorer(records)

    report += f"\nTop Scorer:\n{name} ({avg})\n"

    report += "\nPassing Students:\n"

    for student in passing_students(records):
        report += f"{student}\n"

    return report


