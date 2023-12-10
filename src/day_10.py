from utils import read_input


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile,
# but your sketch doesn't show what shape the pipe has.


# dict with locations and possible connectors
loc_dict = {
    "above": ("|", "F", "7"),
    "below": ("|", "L", "J"),
    "left": ("-", "F", "L"),
    "right": ("-", "J", "7"),
}

# dict with pipes and possible connection locations
pipe_dict = {
    "|": ("above", "below"),
    "-": ("left", "right"),
    "L": ("above", "right"),
    "J": ("left", "above"),
    "7": ("left", "below"),
    "F": ("below", "right"),
}


def extract_data(line):
    return [pos for pos in line]


def search_grid_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return (x, y)


def search_pipes(grid, pos, prev_pos=False):
    neighbours = {}

    # Check above
    if pos[1] > 0:
        # neighbours.append((pos[0], pos[1] - 1))
        neighbours["above"] = (pos[0], pos[1] - 1)

    # Check below
    if pos[1] < len(grid) - 1:
        # neighbours.append((pos[0], pos[1] + 1))
        neighbours["below"] = (pos[0], pos[1] + 1)

    # Check left
    if pos[0] > 0:
        # neighbours.append((pos[0] - 1, pos[1]))
        neighbours["left"] = (pos[0] - 1, pos[1])

    # Check right
    if pos[0] < len(grid[0]) - 1:
        # neighbours.append((pos[0] + 1, pos[1]))
        neighbours["right"] = (pos[0] + 1, pos[1])

    # return both connections
    if not prev_pos:
        connectors = []
        for neighbour, value in neighbours.items():
            if grid[value[1]][value[0]] in loc_dict[neighbour]:
                connectors.append((value))
        return connectors

    else:
        # print(pos)
        # print(neighbours)
        dict_con = [
            value
            for key, values in pipe_dict.items()
            if grid[pos[1]][pos[0]] in key
            for value in values
        ]

        # print(f"{grid[pos[1]][pos[0]]}: {dict_con}")
        neighbours_filtered = {
            key: value for key, value in neighbours.items() if key in dict_con
        }
        # print(neighbours_filtered)
        for key, value in neighbours_filtered.items():
            if value != prev_pos:
                return value


# searches and counts nest tiles
def search_nest(grid, loop):
    nests = 0
    in_loop = False
    # print(loop)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in loop:
                current_char = grid[y][x]
                # print(f"{current_char}: ({x},{y})")
                if current_char == "|":
                    in_loop = not in_loop
                else:
                    if x + 1 < len(grid[y]):
                        next_char = grid[y][x + 1]
                        if current_char == "F":
                            z = 2
                            while next_char == "-":
                                next_char = grid[y][x + z]
                                z += 1
                            if next_char == "J":
                                in_loop = not in_loop
                                # print(f"flip: current{current_char}, next{next_char}")

                        if current_char == "L":
                            z = 2
                            while next_char == "-":
                                next_char = grid[y][x + z]
                                z += 1
                            if next_char == "7":
                                in_loop = not in_loop
                                # print(f"flip: current{current_char}, next{next_char}")

            # count nest if in loop
            # print(in_loop)
            if in_loop and (x, y) not in loop:
                # print("nest plus 1")
                nests += 1

    return nests


input_grid = read_input(10, extract_data, False)

# part 1
grid_start = search_grid_start(input_grid)
connectors = search_pipes(input_grid, grid_start)
pos_list_1 = [grid_start, connectors[0]]
pos_list_2 = [grid_start, connectors[1]]
steps = 1
while pos_list_1[-1] != pos_list_2[-1]:
    pos_list_1.append(search_pipes(input_grid, pos_list_1[-1], pos_list_1[-2]))
    pos_list_2.append(search_pipes(input_grid, pos_list_2[-1], pos_list_2[-2]))
    steps += 1
    # print(pos_list_1)
    # print(pos_list_2)
    # print(steps)
print(steps)


# part 2
input_grid_pt2 = input_grid
input_grid_pt2[grid_start[1]][grid_start[0]] = "|"
loop_list = pos_list_1 + list(reversed(pos_list_2[1:-1]))
nests = search_nest(input_grid_pt2, loop_list)
print(nests)
