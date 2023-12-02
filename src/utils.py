import os


def sum_array(arr):
    return sum(int(num) for num in arr)


def read_input(day, transformer=str, example=False):
    """
    Given a day number (1-25), reads the corresponding input file into
    a list with each line as an item.

    Runs transformer function on each item.
    """
    try:
        if example:
            filename = f"day_{day}_example.txt"
        else:
            filename = f"day_{day}.txt"
        with open(os.path.join("..", "inputs", filename)) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    read_input(1, str, True)
