from utils import read_multisection_input, section_to_grid, flip_grid, sum_array
from time import perf_counter
from copy import deepcopy


def compare_lines(line1, line2):
    for x in range(len(line1)):
        if line1[x] != line2[x]:
            return False
    return True


def search_grid_mirror(grid, original_y=False):
    for y in range(len(grid) - 1):
        mirror = True
        mirror_y = 0
        while mirror:
            # if test:
            # print(y)
            if compare_lines(tuple(grid[y - mirror_y]), tuple(grid[y + 1 + mirror_y])):
                if y - mirror_y == 0 or y + 1 + mirror_y == len(grid) - 1:
                    if original_y is not False:
                        if original_y == y:
                            mirror = False
                        elif original_y != y:
                            return y + 1
                    else:
                        return y + 1
                mirror_y += 1
            else:
                mirror = False
    return False


def search_grid(grid, original_grid=False):
    mirror_y_original = False
    if original_grid:
        mirror_y_original = search_grid_mirror(original_grid)
        if mirror_y_original is not False:
            mirror_y_original -= 1

    mirror_x_original = False
    if original_grid:
        mirror_x_original = search_grid_mirror(flip_grid(original_grid))
        if mirror_x_original is not False:
            mirror_x_original -= 1

    if mirror_y_original is not False:
        mirror_y = search_grid_mirror(grid, mirror_y_original)
    else:
        mirror_y = search_grid_mirror(grid)

    if mirror_x_original is not False:
        mirror_x = search_grid_mirror(flip_grid(grid), mirror_x_original)
    else:
        mirror_x = search_grid_mirror(flip_grid(grid))

    return mirror_x if mirror_x else (mirror_y * 100 if mirror_y else False)


def search_grid_copy(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid_copy = deepcopy(grid)
            if grid_copy[y][x] == "#":
                grid_copy[y][x] = "."
            elif grid_copy[y][x] == ".":
                grid_copy[y][x] = "#"
            search_grid_copy = search_grid(grid_copy, original_grid=grid)
            if search_grid_copy is not False:
                search_grid_original = search_grid(grid)
                if search_grid_copy != search_grid_original:
                    return search_grid_copy


transformers = []
for i in range(100):
    transformers.append(section_to_grid)

grids = read_multisection_input(13, transformers, False)

# part 1
start_time_1 = perf_counter()
answer = []
for grid in grids:
    answer.append(search_grid(grid))

end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(answer)
print(sum_array(answer))
print(f"The execution time is: {execution_time_1}")


start_time_2 = perf_counter()
answer_2 = []

for grid in grids:
    answer_2.append(search_grid_copy(grid))

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(answer_2)
print(sum_array(answer_2))
print(f"The execution time is: {execution_time_2}")
