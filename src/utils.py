import os


def sum_array(arr):
    """
    Given a list with ints, returns the sum
    """
    return sum(int(num) for num in arr)


def section_to_grid(section):
    """
    Given a section of data, returns as a grid (list of lists)
    """
    grid = []
    lines = section.splitlines()
    for y in lines:
        line = []
        for x in y:
            line.append(x)
        grid.append(line)
    return grid


def flip_grid(grid):
    """
    Given a grid (list of lists) returns the grid with the x and y axis flipped
    """
    flipped_grid = []
    for colnum in range(len(grid[0])):
        col = [row[colnum] for row in grid]
        flipped_grid.append(col)
    return flipped_grid


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


def read_multisection_input(day, transformers, example=False):
    """
    Given a day number (1-25), reads the corresponding input file, splits by empty line
    and runs a transformer function from `transformers` list
    for each section and returns a list of section outputs
    """
    try:
        if example:
            filename = f"day_{day}_example.txt"
        else:
            filename = f"day_{day}.txt"
        with open(os.path.join("..", "inputs", filename)) as input_file:
            output = []
            sections = input_file.read().split("\n\n")
            if transformers:
                for idx, section in enumerate(sections):
                    output.append(transformers[idx](section))
            else:
                output = sections
            return output
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    read_input(1, str, True)
