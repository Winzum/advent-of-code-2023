from utils import read_input, sum_array


def find_adjacent_symbols(grid, row, col):
    for y in range(row - 1, row + 2):
        for x in range(col - 1, col + 2):
            if (
                0 <= y < len(grid)
                and 0 <= x < len(grid[y])
                and grid[y][x] != "."
                and not grid[y][x].isdigit()
            ):
                return True
    return False


# find a complete number left of the current col in the current row
def find_number_left(line, col):
    x = col
    while x >= 0:
        if not (line[x].isdigit()) and x != col:
            x += 1
            break
        if x == 0:
            break
        x -= 1
    # print(f"appended: {row[x:col]}")
    if line[col].isdigit():
        col += 1
    return line[x:col]


# look for part numbers in a grid
def search_part_numbers(grid):
    part_numbers = []
    for y in range(len(grid)):
        found_symbol = False
        for x in range((len(grid[y]))):
            # only look for adjacent symbols when found a digit
            if grid[y][x].isdigit():
                if find_adjacent_symbols(grid, y, x):
                    found_symbol = True
            # if the line ends or a period is found, append
            if found_symbol and (x == len(grid[y]) - 1 or not grid[y][x].isdigit()):
                part_numbers.append(find_number_left(grid[y], x))
                found_symbol = False
    return part_numbers


# search for adjacent digits, returns array of numbers
def find_adjacent_numbers(grid, row, col):
    numbers = []

    for y in range(row - 1, row + 2):
        found = False
        for x in range(col - 1, col + 2):
            if (
                0 <= y < len(grid)
                and 0 <= x < len(grid[y])
                and grid[y][x] != "*"
                and grid[y][x].isdigit()
            ):
                found = True

            # if found or end of line, get full number
            if found and (x == col + 1 or not grid[y][x].isdigit()):
                x_found = x
                while grid[y][x_found].isdigit() and x_found < len(grid[y]):
                    x_found += 1
                numbers.append(find_number_left(grid[y], x_found))

    # drop empty entries
    filtered_numbers = [number for number in numbers if bool(number)]
    return filtered_numbers


# look for gear ratios in a grid
def search_gear_ratios(grid):
    gear_ratios = []
    for y in range(len(grid)):
        # found_digit = False
        for x in range((len(grid[y]))):
            # only look for adjacent symbols when found a *
            if grid[y][x] == "*":
                gear_ratio = find_adjacent_numbers(grid, y, x)
                if len(gear_ratio) == 2:
                    gear_ratios.append(int(gear_ratio[0]) * int(gear_ratio[1]))
                #   gear_ratios.append()
    return gear_ratios


# hack to prevent out of bounds
def prepare_data(line):
    return f".{line}."


input_grid = read_input(3, prepare_data, False)

# part 1
found_part_numbers = search_part_numbers(input_grid)
# print(found_part_numbers)
print(sum_array(found_part_numbers))

# part 2
found_gear_ratios = search_gear_ratios(input_grid)
# print(found_gear_ratios)
print(sum_array(found_gear_ratios))
