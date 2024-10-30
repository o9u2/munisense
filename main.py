def extract_digits(filename):
    input_digits = []

    with open(filename, 'r') as f:
        # 'For' loop for less memory usage.
        for line in f:
            # Allows for list only including strings with integer(s).
            if any(char.isdigit() for char in line):
                # Concatenate digits as integer for less memory usage.
                digits = int(''.join([char for char in line if char.isdigit()]))
                input_digits.append(digits)
    
    return input_digits

# def integer_concatination(input_digits):
    

def main():
    filename = 'input.txt'
    digits = extract_digits(filename)
    print(digits)

if __name__ == "__main__":
    main()
