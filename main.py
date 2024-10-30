def extract_input_numbers(filename):
    input_numbers = []

    with open(filename, 'r') as f:
        # 'For' loop for less memory usage.
        for line in f:                                                                      # Allows for list only including strings with digit(s).
            if any(char.isdigit() for char in line):
                number = ''.join([char for char in line if char.isdigit()])                 # To create a list of numbers by omitting letters.
                number_digits = list(number)
                digits = [int(char) for char in number_digits]
                input_numbers.append(digits)
    return input_numbers

def main():
    filename = 'input.txt'
    list_of_numbers = extract_input_numbers(filename)
    print(list_of_numbers)

if __name__ == "__main__":
    main()
