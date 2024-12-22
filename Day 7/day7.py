from pathlib import Path
from itertools import product

def read_input_file(file_path):
    """
    Reads the input file and parses the data into two arrays:
    1. An array of target output values.
    2. An array of input numbers for each target output.

    Args:
        file_path (Path): Path to the input file.

    Returns:
        tuple: A tuple containing two lists:
               - outputs (list of int): Target output values.
               - inputs (list of list of int): Input numbers for each target output.
    """
    outputs, inputs = [], []

    with open(file_path, 'r') as f:
        for line in f:
            output, input_numbers = int(line.split(": ")[0]), [int(x) for x in line.split(": ")[1].split()]
            outputs.append(output)
            inputs.append(input_numbers)

    return outputs, inputs


def is_valid(output, inputs):
    """
    Determines if a combination of operators (+, *, ||) applied left-to-right
    on the inputs can produce the target output.

    Args:
        output (int): The target output value.
        inputs (list of int): The input numbers to evaluate.

    Returns:
        bool: True if the target output can be produced, otherwise False.
    """
    # Generate all possible combinations of operators for len(inputs) - 1 positions
    operators = product(['+', '*', '||'], repeat=len(inputs) - 1)

    # Test each combination of operators
    for ops in operators:
        result = inputs[0]  # Start with the first number
        for i, op in enumerate(ops):
            if op == '+':
                result += inputs[i + 1]
            elif op == '*':
                result *= inputs[i + 1]
            elif op == '||':  # Concatenation operator
                result = int(str(result) + str(inputs[i + 1]))
        
        # If the current operator combination matches the output, return True
        if result == output:
            return True

    # If no operator combination produces the output, return False
    return False


def main():
    """
    Main function to compute the total calibration result by summing
    all outputs that can be validated using the input numbers.
    """
    # Define the input file path
    input_file = Path(__file__).parent / 'input.txt'

    # Read and parse the input data
    outputs, inputs = read_input_file(input_file)

    # Compute the total calibration result
    total_calibration_result = sum(output for i, output in enumerate(outputs) if is_valid(output, inputs[i]))

    # Print the result
    print(total_calibration_result)


if __name__ == "__main__":
    main()