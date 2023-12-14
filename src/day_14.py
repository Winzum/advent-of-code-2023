from utils import read_input, sum_array
from time import perf_counter
from copy import deepcopy
from pprint import pprint


# searches a given grid for a given icon and returns a list of tuples
def get_icon_coordinates(grid, icon):
    icon_list = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == icon:
                icon_list.append((x, y))
    return icon_list


# tilts given balls and blocks north and returns the final situation
def tilt_north(balls, blocks):
    balls_copy = deepcopy(balls)
    for idx, ball in enumerate(balls):
        # closest block above the current ball
        blocks_y = [y for x, y in blocks if x == ball[0] and y < ball[1]]
        block_y = blocks_y[-1] if blocks_y else -1

        # closest ball above the current ball
        balls_y = [y for x, y in balls_copy if x == ball[0] and y < ball[1]]
        ball_y = balls_y[-1] if balls_y else -1

        if ball_y > block_y:
            balls_copy[idx] = (ball[0], ball_y + 1)

        elif block_y > ball_y:
            balls_copy[idx] = (ball[0], block_y + 1)
        else:
            balls_copy[idx] = (ball[0], 0)

    return balls_copy


# returns a list of loads based on a list of balls
def calculate_load(balls, y_length):
    total_load = []
    for ball_x, ball_y in balls:
        total_load.append(y_length - ball_y)
    return total_load


start_time_1 = perf_counter()
input_grid = read_input(14, lambda x: [y for y in x], False)
balls = get_icon_coordinates(input_grid, "O")
balls.sort()
blocks = get_icon_coordinates(input_grid, "#")
blocks.sort()
# pprint(balls)
# pprint(blocks)

# part 1
balls_tilted = tilt_north(balls, blocks)
print(sum_array(calculate_load(balls_tilted, len(input_grid))))

end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")
