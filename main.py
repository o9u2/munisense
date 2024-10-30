def extract_input_numbers(filename):
    input_numbers = []

    with open(filename) as f:                                                               # 'For' loop to prevent loading all data into memory.
        for line in f:                                                                      # Creating list only digit(s).
            if any(char.isdigit() for char in line):
                number = ''.join([char for char in line if char.isdigit()])                 
                number_digits = list(number)
                digits = [char for char in number_digits]                                   
                input_numbers.append(digits)
    return input_numbers


def concat_first_last_digit(list_of_numbers):
    concatted_list = []
    for i, inner_list in enumerate(list_of_numbers):
        first_digit = inner_list[0]
        last_digit = inner_list[-1]
        concatenated = int(first_digit + last_digit)                                        # Convert strings to integers for less memory usage and numerical operations.
        concatted_list.append([concatenated])
    return concatted_list


def main():
    filename = 'input.txt'
    list_of_numbers = extract_input_numbers(filename)
    first_and_last = concat_first_last_digit(list_of_numbers)
    calibration_sum = sum(first_and_last)
    print(calibration_sum)

if __name__ == "__main__":
    main()
