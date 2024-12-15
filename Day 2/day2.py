"""
Example first three lines from .txt file:
9 12 14 16 17 18 15
86 88 91 94 95 95
15 18 20 21 23 25 28 32
"""

import os
from pathlib import Path

def is_safe(report):
    """Check if a report is safe according to the rules."""
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    # Check for strictly increasing or strictly decreasing
    is_increasing = all(1 <= diff <= 3 for diff in diffs)
    is_decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    """Check if a report can be made safe by removing one level."""
    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(reports):
    """Count the number of safe reports, including those made safe by the dampener."""
    safe_count = 0
    for report in reports:
        if is_safe(report) or is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

def read_input_file(file_path):
    """Read the puzzle input from a file."""
    with open(file_path, 'r') as f:
        return [[int(num) for num in line.strip().split()] for line in f]

def main():
    """Main function to process the input file and count safe reports."""
    input_file = Path(__file__).parent / 'input.txt'

    # Read the reports from the input file
    reports = read_input_file(input_file)

    # Count safe reports
    num_safe_reports = sum(is_safe(report) for report in reports)
    num_safe_with_dampener = count_safe_reports_with_dampener(reports)

    print("Safe reports:", num_safe_reports)
    print("Safe reports with dampener:", num_safe_with_dampener)

if __name__ == "__main__":
    main()
