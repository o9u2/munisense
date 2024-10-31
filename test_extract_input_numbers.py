from calibration import extract_input_numbers
from unittest.mock import mock_open, patch

def test_extract_input_numbers():
    input_data = "1abc2"
    expected_output = [['1', '2']]

    with patch('builtins.open', mock_open(read_data=input_data)):       # Using unittest.mock to keep test isolated from external test data.
        result = extract_input_numbers('dummy_filename.txt')
        assert result == expected_output
