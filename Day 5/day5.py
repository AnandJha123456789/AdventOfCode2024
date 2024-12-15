import os
from pathlib import Path

def is_update_valid(ordering, update):
    """
    Checks if the given update is valid based on the ordering rules.
    An update is valid if all dependencies of a page appear before it in the update.

    Args:
        ordering (dict): Dependency rules where key depends on the values in the list.
        update (list): The update sequence to validate.

    Returns:
        bool: True if the update is valid, False otherwise.
    """
    for i, curr_value in enumerate(update):
        # Find indices of dependencies for the current page in the update
        indices = [update.index(num) for num in ordering.get(curr_value, []) if num in update]

        # If any dependency appears later in the update, return False
        if any(i >= index for index in indices):
            return False

    return True

def modify_update(ordering, update):
    """
    Reorders the given update based on the ordering rules using a set and a result list.
    The middle page of the corrected update is returned.

    Args:
        ordering (dict): Dependency rules where key depends on the values in the list.
        update (list): The update sequence to correct.

    Returns:
        int: The middle page value of the corrected update.
    """
    sorted_update = []
    update_set = set(update)  # Convert update to a set for fast lookup
    added = set()  # Tracks pages already added to the sorted update

    # Reorder pages based on their dependencies
    while len(sorted_update) < len(update):
        for page in update:
            if page not in added:
                # Add page if all its dependencies are already in sorted_update
                if page not in ordering or all(dep in added for dep in ordering[page] if dep in update_set):
                    sorted_update.append(page)
                    added.add(page)

    # Return the middle page of the corrected update
    return sorted_update[len(sorted_update) // 2]

def read_input_file(file_path):
    """
    Reads the puzzle input from a file and parses it into ordering rules and updates.

    Args:
        file_path (str): Path to the input file.

    Returns:
        tuple: A tuple containing:
            - ordering (dict): Dependency rules where key depends on the values in the list.
            - updates (list): List of updates to validate and correct.
    """
    ordering = {}
    updates = []

    with open(file_path, 'r') as f:
        getting_ordering = True  # Flag to distinguish ordering rules and updates

        for line in f:
            line = line.strip()
            if not line:
                getting_ordering = False  # Empty line separates rules from updates
            elif getting_ordering:
                # Parse ordering rules
                first, second = map(int, line.split('|'))
                ordering.setdefault(first, []).append(second)
            else:
                # Parse updates
                updates.append(list(map(int, line.split(','))))

    return ordering, updates

def main():
    """
    Main function to process the input file and compute sums for Part 1 and Part 2.
    """
    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    ordering, updates = read_input_file(input_file)

    # Initialize sums for Part 1 and Part 2
    part_1_sum = 0
    part_2_sum = 0

    # Process each update
    for update in updates:
        if is_update_valid(ordering, update):
            # If valid, add the middle page value to Part 1 sum
            part_1_sum += update[len(update) // 2]
        else:
            # If invalid, correct it and add the middle page value to Part 2 sum
            part_2_sum += modify_update(ordering, update)

    # Print the results
    print(f"Part 1 Sum: {part_1_sum}")
    print(f"Part 2 Sum: {part_2_sum}")

if __name__ == "__main__":
    main()
