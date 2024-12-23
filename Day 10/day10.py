from pathlib import Path
import subprocess

# Direction vectors for moving up, down, left, and right
dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def read_input_file(file_path):
    """
    Reads the input file and returns the grid as a list of lists.
    """
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]
    
def in_grid(grid, row, col):
    """
    Checks if a given position (row, col) is within the bounds of the grid.
    """
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    
def get_trailhead_locations(grid):
    """
    Finds all positions in the grid that are trailheads (height '0').
    """
    trailhead_locations = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '0':
                trailhead_locations.append((row, col))

    return trailhead_locations

def get_scores(grid, trailhead_locations):
    scores = []

    for trailhead in trailhead_locations:
        score = 0

        # Do DFS to get to the number 9, ensuring that we only go up by 1 at a time
        stack = [trailhead]
        visited = set()
        while stack:
            i, j = stack.pop()

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if grid[i][j] == '9':
                score += 1
                continue

            for di, dj in dd:
                new_i, new_j = i + di, j + dj
                
                if not in_grid(grid, new_i, new_j):
                    continue

                if int(grid[new_i][new_j]) != int(grid[i][j]) + 1:
                    continue

                stack.append((new_i, new_j))

        scores.append(score)
        
    return scores

def get_ratings(grid, trailhead_locations):
    scores = []

    for trailhead in trailhead_locations:
        score = 0

        stack = [trailhead]
        while stack:
            i, j = stack.pop()

            if grid[i][j] == '9':
                score += 1
                continue

            for di, dj in dd:
                new_i, new_j = i + di, j + dj
                
                if not in_grid(grid, new_i, new_j):
                    continue

                if int(grid[new_i][new_j]) != int(grid[i][j]) + 1:
                    continue

                stack.append((new_i, new_j))

        scores.append(score)
        
    return scores

def main():
    """
    Main function to compute solutions for Part 1 and Part 2.
    """
    # Clear the terminal
    subprocess.run(["cls"], shell=True)

    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    grid = read_input_file(input_file)

    # Find all trailhead locations
    trailhead_locations = get_trailhead_locations(grid)

    # Part 1: Compute the sum of scores for all trailheads
    part_1_scores = get_scores(grid, trailhead_locations)
    print("Part 1:", sum(part_1_scores))

    # Part 2: Compute the sum of ratings for all trailheads
    part_2_ratings = get_ratings(grid, trailhead_locations)
    print("Part 2:", sum(part_2_ratings))

if __name__ == "__main__":
    main()

