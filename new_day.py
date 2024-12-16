# Generate a new day with all files and stuff
import os

basic_text = '''
from pathlib import Path

def read_input_file(file_path):
    """
    Reads the input file and returns the grid as a list of lists.
    """
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def main():
    """
    Main function to compute solutions for Part 1 and Part 2.
    """
    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    grid = read_input_file(input_file)

if __name__ == "__main__":
    main()

'''

day_numbers = [(str(i)) for i in list(range(1,26))]

for day_number in day_numbers:
    # Create the directory for the new day if it doesn't exist
    if not os.path.exists(f"Day {day_number}"):
        os.mkdir(f"Day {day_number}")
        print(f"Created directory for Day {day_number}")

    # Create the input file for the new day if it doesn't exist
    if not os.path.exists(f"Day {day_number}/input.txt"):
        with open(f"Day {day_number}/input.txt", "w") as f:
            print(f"Created input file for Day {day_number}")
            pass

    # Create the dayn.py file for the new day if it doesn't exist
    if not os.path.exists(f"Day {day_number}/day{day_number}.py"):
        with open(f"Day {day_number}/day{day_number}.py", "w") as f:
            f.write(basic_text)
            print(f"Created day{day_number}.py for Day {day_number}")