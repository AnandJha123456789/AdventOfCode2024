from pathlib import Path
import subprocess

def read_input_file(file_path):
    """
    Reads the input file and returns the single line of text.
    """
    with open(file_path, 'r') as f:
        return f.readline().strip()

def build_disk(line):
    """
    Constructs the initial disk representation based on the input line.
    The disk is a list where file blocks are integers and free space is None.
    """
    disk = []
    curr_value = 0

    for i, char in enumerate(line):
        if i % 2 == 1:
            # Add free space blocks (None)
            disk.extend([None] * int(char))
            curr_value += 1
        else:
            # Add file blocks (integers)
            disk.extend([curr_value] * int(char))

    return disk

def rearrange_disk(disk):
    """
    Rearranges the disk by moving file blocks to the leftmost free space.
    """
    l, r = 0, len(disk) - 1

    # Find the initial leftmost free space and rightmost file block
    while disk[l] is not None:
        l += 1
    while disk[r] is None:
        r -= 1

    # Move file blocks to the leftmost free space
    while l < r:
        disk[l], disk[r] = disk[r], None
        while l < len(disk) and disk[l] is not None:
            l += 1
        while r >= 0 and disk[r] is None:
            r -= 1

    return disk

def get_checksum(disk):
    """
    Calculates the checksum of the disk.
    The checksum is the sum of (position * file ID) for all file blocks.
    """
    return sum(i * block for i, block in enumerate(disk) if block is not None)

def build_disk_part2(line):
    """
    Constructs the disk and free space information for Part 2.
    The disk is a dictionary with file IDs as keys and (start_idx, length) as values.
    The empty_spaces is a list of (start_idx, length) tuples.
    """
    disk = {}
    empty_spaces = []
    curr_idx = 0
    curr_value = 0

    for i, char in enumerate(line):
        if i % 2 == 1:
            empty_spaces.append((curr_idx, int(char)))
            curr_value += 1
        else:
            disk[curr_value] = (curr_idx, int(char))
        curr_idx += int(char)

    return disk, empty_spaces

def rearrange_disk_part2(disk, empty_spaces):
    """
    Rearranges the disk by moving entire files to the leftmost span of free space that fits.
    Processes files in decreasing order of file ID.
    """
    for file_id in sorted(disk.keys(), reverse=True):
        start_idx, length = disk[file_id]

        for i, (empty_start, empty_length) in enumerate(empty_spaces):
            if empty_start >= start_idx:
                break  # Stop if no free space is available to the left

            if length <= empty_length:
                # Move file to this free space
                disk[file_id] = (empty_start, length)
                if length == empty_length:
                    empty_spaces.pop(i)
                else:
                    empty_spaces[i] = (empty_start + length, empty_length - length)
                break

    return disk, empty_spaces

def get_checksum_part2(disk):
    """
    Calculates the checksum for Part 2.
    The checksum is the sum of (position * file ID) for all file blocks.
    """
    checksum = 0

    for file_id, (start_idx, length) in disk.items():
        for i in range(start_idx, start_idx + length):
            checksum += i * file_id

    return checksum

def main():
    """
    Main function to compute solutions for Part 1 and Part 2.
    """
    # Clear the terminal
    subprocess.run(["cls"], shell=True)

    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    line = read_input_file(input_file)

    # Part 1
    disk = build_disk(line)
    modified_disk = rearrange_disk(disk)
    print('Part 1:', get_checksum(modified_disk))

    # Part 2
    disk, empty_spaces = build_disk_part2(line)
    modified_disk, _ = rearrange_disk_part2(disk, empty_spaces)
    print('Part 2:', get_checksum_part2(modified_disk))

if __name__ == "__main__":
    main()