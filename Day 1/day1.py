"""
Example first three lines from .txt file:
69214   60950
83241   49638
37930   31308
"""

from pathlib import Path
from collections import Counter

def read_input_file(file_path):
    """Read the input file and return two lists of integers."""
    left_list, right_list = [], []
    with open(file_path, 'r') as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

print("habibi!")

def calculate_total_distance(left_list, right_list):
    """Calculate the total distance between sorted lists."""
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    return sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

def calculate_similarity_score(left_list, right_list):
    """Calculate the similarity score based on occurrences in the right list."""
    right_counter = Counter(right_list)
    return sum(num * right_counter[num] for num in left_list if num in right_counter)

def main():
    """Main function to calculate and print results."""
    input_file = Path(__file__).parent / 'input.txt'

    # Read input lists
    left_list, right_list = read_input_file(input_file)

    # Part 1: Total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total Distance:", total_distance)

    # Part 2: Similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()
