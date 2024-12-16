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

day_numbers = [(str(i)) for i in list(range(7,26))]

for day_number in day_numbers:
    # Create the directory for the new day
    os.makedirs(f"Day {day_number}", exist_ok=True)

    # Create the input file for the new day
    with open(f"Day {day_number}/input.txt", "w") as f:
        pass

    # Create the main.py file for the new day
    with open(f"Day {day_number}/day{day_number}.py", "w") as f:
        f.write(basic_text)