from pathlib import Path

def read_input_file(file_path):
    """
    Reads the input file and returns the grid as a list of lists.

    Args:
        file_path (str): Path to the input file.

    Returns:
        list: Grid represented as a list of lists.
    """
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def get_hashmap(grid):
    """
    Creates a hashmap where each unique character in the grid is mapped to its coordinates.

    Args:
        grid (list): The input grid.

    Returns:
        dict: A dictionary with characters as keys and a list of their coordinates as values.
    """
    hashmap = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':  # Ignore empty spaces
                hashmap.setdefault(grid[i][j], []).append((i, j))
    return hashmap

def valid_coord(grid, i, j):
    """
    Checks if the given coordinates are within the grid bounds.

    Args:
        grid (list): The grid.
        i (int): Row index.
        j (int): Column index.

    Returns:
        bool: True if the coordinates are valid, False otherwise.
    """
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def place_antinodes(grid, hashmap):
    """
    Computes the number of unique antinode locations for Part 1.

    Args:
        grid (list): The grid.
        hashmap (dict): Map of characters to their coordinates.

    Returns:
        int: Number of unique antinode locations.
    """
    antinode_locations = set()

    for key, coordinates in hashmap.items():
        for i in range(len(coordinates)):
            x, y = coordinates[i]
            for j in range(i + 1, len(coordinates)):
                x1, y1 = coordinates[j]
                dx, dy = x1 - x, y1 - y

                # Calculate potential antinode locations
                location_1 = (x - dx, y - dy)
                location_2 = (x1 + dx, y1 + dy)

                # Add valid locations
                if valid_coord(grid, location_1[0], location_1[1]):
                    antinode_locations.add(location_1)
                    if grid[location_1[0]][location_1[1]] == '.': grid[location_1[0]][location_1[1]] = '#'
                if valid_coord(grid, location_2[0], location_2[1]):
                    if grid[location_2[0]][location_2[1]] == '.': grid[location_2[0]][location_2[1]] = '#'
                    antinode_locations.add(location_2)

    return len(antinode_locations)

def place_antinodes_part_2(grid, hashmap):
    """
    Computes the number of unique antinode locations for Part 2.

    Args:
        grid (list): The grid.
        hashmap (dict): Map of characters to their coordinates.

    Returns:
        int: Number of unique antinode locations.
    """
    antinode_locations = set()

    for key, coordinates in hashmap.items():
        for i in range(len(coordinates)):
            x, y = coordinates[i]
            for j in range(i + 1, len(coordinates)):
                x1, y1 = coordinates[j]
                dx, dy = x1 - x, y1 - y

                # Trace antinodes in both directions
                location_1 = (x, y)
                location_2 = (x1, y1)

                while valid_coord(grid, location_1[0], location_1[1]):
                    antinode_locations.add(location_1)
                    if grid[location_1[0]][location_1[1]] == '.': grid[location_1[0]][location_1[1]] = '#'
                    location_1 = (location_1[0] - dx, location_1[1] - dy)

                while valid_coord(grid, location_2[0], location_2[1]):
                    antinode_locations.add(location_2)
                    if grid[location_2[0]][location_2[1]] == '.': grid[location_2[0]][location_2[1]] = '#'
                    location_2 = (location_2[0] + dx, location_2[1] + dy)

    return len(antinode_locations)

def main():
    """
    Main function to compute solutions for Part 1 and Part 2.
    """
    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    grid = read_input_file(input_file)

    # Generate hashmap of antenna locations
    hashmap = get_hashmap(grid)

    # Compute and print results
    print("Part 1:", place_antinodes(grid.copy(), hashmap))
    print("Part 2:", place_antinodes_part_2(grid.copy(), hashmap))

if __name__ == "__main__":
    main()
