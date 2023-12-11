from utils import read_input, sum_array


def split_line(line):
    return [x for x in line]


# takes a grid and expands where only rows or columns with a sign are found
def expand_empty(grid, sign):
    expand_y = []
    for y in range(len(grid)):
        if all(point == sign for point in grid[y]):
            expand_y.append(y)

    # flip the grid 1 quarter clockwise
    expand_x = []
    flipped_grid = []
    for colnum in range(len(grid[0])):
        col = [row[colnum] for row in grid]
        flipped_grid.append(col)

    for x in range(len(flipped_grid)):
        if all(point == sign for point in flipped_grid[x]):
            expand_x.append(x)

    # expand x
    expanded_grid = grid
    expand_x.reverse()
    # print(expand_x)
    for y in range(len(grid)):
        for x in expand_x:
            expanded_grid[y].insert(x, sign)

    # expand y
    expand_y.reverse()
    # print(expand_y)
    for y in expand_y:
        expanded_grid.insert(y, expanded_grid[y])

    # return the empty rows and cols for part 2
    expand_x.reverse()
    expand_y.reverse()
    return expanded_grid, expand_x, expand_y


# search a grid for a particular sign and returns a list of tuples
def search_sign(grid, sign):
    sign_list = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == sign:
                sign_list.append((x, y))

    return sign_list


# thanks wikipedia
def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)


def calculate_shortest_distances(coordinates):
    n = len(coordinates)
    shortest_distances = {}

    for i in range(n):
        for j in range(i + 1, n):
            point1, point2 = coordinates[i], coordinates[j]
            if not (
                (point1, point2) in shortest_distances
                or (point2, point1) in shortest_distances
            ):
                distance = manhattan_distance(point1, point2)
                shortest_distances[(point1, point2)] = distance

    return shortest_distances


# expands coordinates by a set amount based on empty rows and cols
def expand_coordinates(coordinates, expand_y, expand_x, amount):
    for idx, (x, y) in enumerate(coordinates):
        new_x = x
        new_y = y
        for exp_x in expand_x:
            if x > exp_x:
                # print(f"{x} > {exp_x}")
                new_x += amount - 1
        for exp_y in expand_y:
            if y > exp_y:
                new_y += amount - 1
        coordinates[idx] = (new_x, new_y)
    return coordinates


input_grid = read_input(11, split_line, False)

# part 1
expanded_grid, expand_x, expand_y = expand_empty(input_grid, ".")
galaxy_list = search_sign(expanded_grid, "#")
shortest_distances = calculate_shortest_distances(galaxy_list)
print(sum_array([n for n in shortest_distances.values()]))

# part 2
input_grid_2 = read_input(11, split_line, False)
unexpanded_galaxy_list = search_sign(input_grid_2, "#")
# print(unexpanded_galaxy_list)
expanded_galaxy_list = expand_coordinates(
    unexpanded_galaxy_list, expand_y, expand_x, 1000000
)
shortest_distances_2 = calculate_shortest_distances(expanded_galaxy_list)
print(sum_array([n for n in shortest_distances_2.values()]))
