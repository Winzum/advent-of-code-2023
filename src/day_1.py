from utils import read_input

number_dict = {
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "fo4r",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}


def replace_with_dict(input_string, replacement_dict):
    for key, value in replacement_dict.items():
        if key in input_string:
            input_string = input_string.replace(key, value)
    return input_string


def extract_int(line):
    line = replace_with_dict(line, number_dict)
    print(line)

    result_digits = [char for char in line if char.isdigit()]

    # return the first and last digit
    return f"{result_digits[0]}{result_digits[-1]}"


def sum_array(arr):
    return sum(int(num) for num in arr)


numbers = read_input(1, extract_int, False)
print(numbers)
print(sum_array(numbers))
