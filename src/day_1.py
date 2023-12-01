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


def replace_with_dict(input_string, dict):
    for key, value in dict.items():
        if key in input_string:
            input_string = input_string.replace(key, value)
    return input_string


def extract_int(line):
    result = ""
    line = replace_with_dict(line, number_dict)
    print(line)
    for char in line:
        if char.isdigit():
            result += char
    # return the first and last digit
    return f"{result[0]}{result[len(result)-1]}"


def sum_array(arr):
    result = 0
    for num in arr:
        num = int(num)
        result = result + num
        # print(result)
    return result


numbers = read_input(1, extract_int, False)
print(numbers)
print(sum_array(numbers))
