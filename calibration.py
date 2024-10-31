def extract_input_numbers(filename):
    input_numbers = []
    with open(filename) as f:
        for line in f:
            digits = [char for char in line if char.isdigit()]
            if digits:
                input_numbers.append(digits)
    return input_numbers


def concat_first_last_digit(list_of_numbers):
    return [int(inner_list[0] + inner_list[-1]) for inner_list in list_of_numbers]


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
