from pathlib import Path

def count_word_in_grid(grid, word):
    """Count all occurrences of a word in the grid in all directions."""
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1), # Diagonal up-left
    ]
    count = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if the word can fit in this direction
                if all(
                    is_valid(r + dr * i, c + dc * i) and grid[r + dr * i][c + dc * i] == word[i]
                    for i in range(word_len)
                ):
                    count += 1

    return count

def count_xmas_in_grid(grid):
    """Count all occurrences of X-MAS patterns in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    # Helper function to check if indices are valid
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Check for the X-MAS pattern at a given center (r, c)
    def is_xmas_center(r, c):
        patterns = [
            ((-1, -1, "M"), (0, 0, "A"), (1, 1, "S"), (-1, 1, "M"), (1, -1, "S")),
            ((-1, -1, "M"), (0, 0, "A"), (1, 1, "S"), (-1, 1, "S"), (1, -1, "M")),
            ((-1, -1, "S"), (0, 0, "A"), (1, 1, "M"), (-1, 1, "S"), (1, -1, "M")),
            ((-1, -1, "S"), (0, 0, "A"), (1, 1, "M"), (-1, 1, "M"), (1, -1, "S"))
        ]
        for pattern in patterns:
            if all(is_valid(r + dr, c + dc) and grid[r + dr][c + dc] == char for dr, dc, char in pattern):
                return True
        return False

    # Scan the grid for all possible centers
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A" and is_xmas_center(r, c):
                xmas_count += 1

    return xmas_count

def read_input_file(file_path):
    """Read the input file and return the grid as a list of strings."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def main():
    """Main function to read input, process the word search, and calculate the result."""
    input_file = Path(__file__).parent / 'input.txt'
    grid = read_input_file(input_file)
    word = "XMAS"

    # Count occurrences of the word in the grid
    total_occurrences = count_word_in_grid(grid, word)
    print("Total occurrences of the word XMAS:", total_occurrences)

    # Part 2: Count occurrences of X-MAS patterns
    xmas_occurrences = count_xmas_in_grid(grid)
    print("Total occurrences of X-MAS patterns:", xmas_occurrences) 

if __name__ == "__main__":
    main()
