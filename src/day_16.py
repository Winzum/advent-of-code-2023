from utils import read_input
from time import perf_counter


# simulates beams over grid and returns energized tiles
def simulate_energized_tiles(grid, first_beam):
    limit_y, limit_x = len(grid), len(grid[0])
    beams = set()
    visited_mirrors = set()
    energized_tiles = set()
    energized_tiles.add((first_beam[0], first_beam[1]))

    def is_valid(x, y):
        return 0 <= x < limit_x and 0 <= y < limit_y

    def reflect(direction, mirror):
        # print("reflect")
        if mirror == "/":
            return (-direction[1], -direction[0])
        elif mirror == "\\":
            return (direction[1], direction[0])

    def simulate():
        nonlocal beams, energized_tiles, visited_mirrors
        new_beams = set()
        for x, y, direction in beams:
            new_x, new_y = x + direction[0], y + direction[1]

            if is_valid(new_x, new_y):
                if (new_x, new_y) not in energized_tiles:
                    energized_tiles.add((new_x, new_y))

                tile = grid[new_y][new_x]

                match tile:
                    case "\\" | "/":
                        if (new_x, new_y, direction) not in visited_mirrors:
                            new_direction = reflect(direction, tile)
                            new_beams.add((new_x, new_y, new_direction))
                            visited_mirrors.add((new_x, new_y, direction))

                    case "-":
                        if direction[0] == 0:
                            if (new_x, new_y, direction) not in visited_mirrors:
                                new_beams.add(
                                    (new_x, new_y, (direction[1], direction[0]))
                                )
                                new_beams.add(
                                    (new_x, new_y, (-direction[1], direction[0]))
                                )
                                visited_mirrors.add((new_x, new_y, direction))
                        else:
                            new_beams.add((new_x, new_y, direction))
                    case "|":
                        if direction[1] == 0:
                            if (new_x, new_y, direction) not in visited_mirrors:
                                new_beams.add(
                                    (new_x, new_y, (direction[1], direction[0]))
                                )
                                new_beams.add(
                                    (new_x, new_y, (direction[1], -direction[0]))
                                )
                                visited_mirrors.add((new_x, new_y, direction))
                        else:
                            new_beams.add((new_x, new_y, direction))
                    case _:
                        new_beams.add((new_x, new_y, direction))

        beams = new_beams
        # print(beams)

    # first beams moves right in case of example, down in case of prod
    beams.add((first_beam))

    # limit the loops
    while len(beams) > 0:
        simulate()

    return energized_tiles


# input_grid = read_input(16, lambda line: [x for x in line], example)
input_grid = read_input(16, str, False)
# print(input_grid)

# part 1
start_time_1 = perf_counter()
result = simulate_energized_tiles(input_grid, (0, 0, (0, 1)))
print(len(result))
end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()
largest = []
for y in range(len(input_grid)):
    largest.append(len(simulate_energized_tiles(input_grid, (0, y, (1, 0)))))
    largest.append(
        len(simulate_energized_tiles(input_grid, (len(input_grid[y]) - 1, y, (-1, 0))))
    )
for x in range(len(input_grid[0])):
    largest.append(len(simulate_energized_tiles(input_grid, (x, 0, (0, 1)))))
    largest.append(
        len(simulate_energized_tiles(input_grid, (x, len(input_grid) - 1, (0, -1))))
    )

# print(largest)
print(max(largest))

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
