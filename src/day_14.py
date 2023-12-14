from utils import read_input
from time import perf_counter


# searches a given grid for a given icon and returns a dict with a set
def get_icon_coordinates(grid, icon):
    icon_dict = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == icon:
                if x in icon_dict:
                    icon_dict[x].add((y))
                else:
                    icon_dict[x] = {y}
    return icon_dict


def falling_balls(ball_set, block_set={}):
    result = set()
    for ball in ball_set:
        while ball > 0:
            ball -= 1
            if ball in block_set or ball in result:
                ball += 1
                break
        while ball in result:
            ball += 1
        result.add(ball)
    return result


# tilts given balls and blocks north and returns the final situation
def tilt_north(balls, blocks):
    for x in balls.keys():
        block_set = blocks[x] if x in blocks else {}
        balls[x] = falling_balls(balls[x], block_set)

    return balls


# rotates a dict a quarter clockwise
def rotate_quarter_clockwise(input_dict, max_y):
    rotated_dict = {}
    for x, y_set in input_dict.items():
        for y in y_set:
            new_x = max_y - y
            new_y = x

            if new_x not in rotated_dict:
                rotated_dict[new_x] = set()
            rotated_dict[new_x].add(new_y)

    return rotated_dict


# one cycle of north, west, south, east
def cycle_balls_blocks(balls, blocks, max_line):
    for i in range(4):
        balls = tilt_north(balls, blocks)
        balls = rotate_quarter_clockwise(balls, max_line)
        blocks = rotate_quarter_clockwise(blocks, max_line)
    return balls, blocks


# returns a list of loads based on a list of balls
def calculate_load(balls, y_length):
    return sum(
        (y_length - element) for key_set in balls.values() for element in key_set
    )


start_time_1 = perf_counter()
input_grid = read_input(14, lambda x: [y for y in x], False)

balls = get_icon_coordinates(input_grid, "O")
blocks = get_icon_coordinates(input_grid, "#")

# part 1
balls_tilted = tilt_north(balls, blocks)
print(calculate_load(balls_tilted, len(input_grid)))

end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")


# part 2
start_time_2 = perf_counter()

# 1000 works as well in my case
for i in range(1000):
    cycle_balls, cycle_blocks = cycle_balls_blocks(balls, blocks, len(input_grid) - 1)
    balls, blocks = cycle_balls, cycle_blocks

print(calculate_load(balls, len(input_grid)))

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
