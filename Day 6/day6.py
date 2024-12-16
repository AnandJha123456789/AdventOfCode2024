from pathlib import Path
import copy
from tqdm import tqdm

def read_input_file(file_path):
    """
    Reads the input file and returns the grid as a list of lists.
    """
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def on_grid(location, grid):
    """
    Checks if the given location is within the boundaries of the grid.
    """
    return 0 <= location[0] < len(grid) and 0 <= location[1] < len(grid[0])

def change_direction_90(direction):
    """
    Rotates the direction 90 degrees clockwise.
    """
    directions = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    return directions[direction]

def calculate_next_location(location, direction):
    """
    Calculates the next location based on the current direction.
    """
    deltas = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
    delta = deltas[direction]
    return (location[0] + delta[0], location[1] + delta[1])

def is_loop(grid, location, direction):
    """
    Checks if adding an obstacle at the current position causes the guard to enter a loop.
    """
    visited_states = set()

    while True:
        state = (location, direction)
        if state in visited_states:
            return True
        visited_states.add(state)

        next_location = calculate_next_location(location, direction)

        if not on_grid(next_location, grid):
            return False

        if grid[next_location[0]][next_location[1]] == '#':
            direction = change_direction_90(direction)
        else:
            location = next_location

def main():
    """
    Main function to compute solutions for Part 1 and Part 2.
    """
    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    grid = read_input_file(input_file)

    # Initial guard direction
    init_direction = 'up'

    # Locate the guard's starting position ('^')
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == '^':
                init_location = (r, c)
                break
        else:
            continue
        break

    # Part 1: Simulate the guard's patrol path
    location = init_location
    direction = init_direction
    visited_spaces = set()
    visited_spaces.add(location)

    while True:
        next_location = calculate_next_location(location, direction)

        if not on_grid(next_location, grid):
            break

        if grid[next_location[0]][next_location[1]] == '#':
            direction = change_direction_90(direction)
        else:
            location = next_location
            visited_spaces.add(location)

    print(f"Part 1 Solution: {len(visited_spaces)}")

    # Part 2: Find possible positions to place an obstruction, where obstructions can only be put on guard's path
    visited_spaces.remove(init_location)
    num_loops = 0

    for space in tqdm(visited_spaces, desc="Completing Part 2"):
        tmp_grid = copy.deepcopy(grid)
        tmp_grid[space[0]][space[1]] = '#'
        if is_loop(tmp_grid, init_location, init_direction):
            num_loops += 1

    print(f"Part 2 Solution: {num_loops}")

if __name__ == "__main__":
    main()
