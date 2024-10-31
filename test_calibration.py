from unittest.mock import (
    mock_open,
    patch,
)  # Using unittest.mock to keep test isolated from external test data.
from calibration import extract_input_numbers
from calibration import concat_first_last_digit
from calibration import sum_calibrators


def test_extract_input_numbers():
    # Test Case: Advent Code input.txt strings input
    input_data = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
    expected_output = [["1", "2"], ["3", "8"], ["1", "2", "3", "4", "5"], ["7"]]

    with patch("builtins.open", mock_open(read_data=input_data)):
        result = extract_input_numbers("dummy_filename.txt")
        assert result == expected_output


def test_concat_first_last_digit():
    # Test Case: Advent Code given example input and output
    input_data = [["1", "2"], ["3", "8"], ["1", "2", "3", "4", "5"], ["7"]]
    expected_output = [12, 38, 15, 77]


def test_sum_calibrators():
    # Test Case 1: Standard input
    input_data = [12, 38, 15, 77]
    expected_output = 142
    result = sum_calibrators(input_data)
    assert result == expected_output

    # Test Case 2: Empty input
    input_data = []
    expected_output = 0
    result = sum_calibrators(input_data)
    assert result == expected_output
