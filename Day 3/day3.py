import re
from pathlib import Path

def extract_valid_mul_instructions_part_1(memory):
    """Extract and evaluate valid mul instructions from the given memory string."""
    # Regular expression to match valid mul instructions (e.g., mul(44,46))
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, memory)

    # Calculate the sum of the products from valid instructions
    return sum(int(x) * int(y) for x, y in matches)

def extract_valid_mul_instructions_part_2(memory):
    """Extract and evaluate valid mul instructions from the given memory string."""
    # Patterns to match control instructions and mul instructions
    control_pattern = r"(do\(\)|don't\(\))"
    mul_pattern = r"mul\((\d+),(\d+)\)"
    combined_pattern = fr"{control_pattern}|{mul_pattern}"

    # Find all matches in sequence
    matches = re.finditer(combined_pattern, memory)

    # Initialize state and result
    is_enabled = True
    total_sum = 0

    for match in matches:
        if match.group(1):  # Control instruction (do() or don't())
            if match.group(1) == "do()":
                is_enabled = True
            elif match.group(1) == "don't()":
                is_enabled = False
        elif match.group(2) and is_enabled:  # Valid mul instruction when enabled
            x, y = int(match.group(2)), int(match.group(3))
            total_sum += x * y

    return total_sum

def read_input_file(file_path):
    """Read the input file and return its content as a single string."""
    with open(file_path, 'r') as f:
        return f.read()

def main():
    """Main function to process the corrupted memory and calculate the sum."""
    input_file = Path(__file__).parent / 'input.txt'

    # Read the corrupted memory from the input file
    corrupted_memory = read_input_file(input_file)

    # Extract and sum valid mul instructions
    part_1_sum = extract_valid_mul_instructions_part_1(corrupted_memory)
    print("Sum of valid mul instructions (part 1):", part_1_sum)

    # Extract and sum valid mul instructions with control instructions
    part_2_sum = extract_valid_mul_instructions_part_2(corrupted_memory)
    print("Sum of valid mul instructions (part 2):", part_2_sum)

if __name__ == "__main__":
    main()
