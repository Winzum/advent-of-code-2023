from utils import read_input
from time import perf_counter


# simulates beams over grid and returns energized tiles
def simulate_energized_tiles(grid, example):
    print(example)
    limit_y, limit_x = len(grid), len(grid[0])
    beams = set()
    energized_tiles = set()
    energized_tiles.add((0, 0))

    def is_valid(x, y):
        return 0 <= x < limit_x and 0 <= y < limit_y

    def reflect(direction, mirror):
        # print("reflect")
        if mirror == "/":
            return (-direction[1], -direction[0])
        elif mirror == "\\":
            return (direction[1], direction[0])

    def simulate():
        nonlocal beams, energized_tiles
        new_beams = set()

        for x, y, direction in beams:
            new_x, new_y = x + direction[0], y + direction[1]

            if is_valid(new_x, new_y):
                if (new_x, new_y) not in energized_tiles:
                    energized_tiles.add((new_x, new_y))

                tile = grid[new_y][new_x]

                match tile:
                    case "\\" | "/":
                        new_direction = reflect(direction, tile)
                        new_beams.add((new_x, new_y, new_direction))
                    case "-":
                        if direction[0] == 0:
                            new_beams.add((new_x, new_y, (direction[1], direction[0])))
                            new_beams.add((new_x, new_y, (-direction[1], direction[0])))
                        else:
                            new_beams.add((new_x, new_y, direction))
                    case "|":
                        if direction[1] == 0:
                            new_beams.add((new_x, new_y, (direction[1], direction[0])))
                            new_beams.add((new_x, new_y, (direction[1], -direction[0])))
                        else:
                            new_beams.add((new_x, new_y, direction))
                    case _:
                        new_beams.add((new_x, new_y, direction))

        # print(new_beams)
        if len(new_beams) == 0:
            quit()
        beams = new_beams

    # first beams moves right in case of example, down in case of prod
    beams.add((0, 0, (1, 0) if example else (0, 1)))

    # limit the loops
    for _ in range(limit_x * limit_y):
        simulate()

    return energized_tiles


example = False
input_grid = read_input(16, lambda line: [x for x in line], example)

# print(input_grid)

# part 1
start_time_1 = perf_counter()
result = simulate_energized_tiles(input_grid, example)
print(len(result))
end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
