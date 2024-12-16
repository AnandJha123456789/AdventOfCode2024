
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

