def extract_input_numbers(filename):
    input_numbers = []
    try:
        with open(filename) as f:
            for line in f:
                digits = [char for char in line if char.isdigit()]
                if digits:
                    input_numbers.append(digits)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise  # Re-raise the exception to allow higher-level handling
    return input_numbers


def concat_first_last_digit(list_of_numbers):
    result = []
    for inner_list in list_of_numbers:
        if not inner_list:
            raise ValueError("Inner list is empty. Nothing to extract.")
        try:
            value = int(inner_list[0] + inner_list[-1])
            result.append(value)
        except (IndexError, ValueError) as e:
            print(f"Error: Index or value error. '{inner_list}': {e}")
            raise
    return result


def sum_calibrators(calibration_values):
    sum_calibration_values = sum(calibration_values)
    return sum_calibration_values


def main():
    filename = "input.txt"
    list_of_numbers = extract_input_numbers(filename)
    calibration_values = concat_first_last_digit(list_of_numbers)

    print(sum_calibrators(calibration_values))


if __name__ == "__main__":
    main()
