input_digits = []

with open('input.txt', 'r') as f:
    # 'For'loop for less memory usage.
    for line in f:
        # Allows for list only including strings w/ integer(s).
        if any(char.isdigit() for char in line):
            # Extract only digits and concatenate them
            digits = ''.join([char for char in line if char.isdigit()])
            input_digits.append(digits)
print(input_digits)