from utils import read_input
from time import perf_counter


direction_dict = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}
direction_hex = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}


def extract_data(line):
    new_line = line.split()
    new_line[0] = direction_dict[new_line[0]]
    new_line[1] = int(new_line[1])
    new_line[2] = new_line[2][1:-1]
    return new_line


# follows a list of dig instructions, constructs a list of coordinates
def follow_dig_instructions(instructions):
    latest_coordinate = (0, 0)
    coordinate_set = []
    coordinate_set.append(latest_coordinate)
    for instruction in instructions:
        new_coordinate = (
            latest_coordinate[0] + instruction[0][0] * instruction[1],
            latest_coordinate[1] + instruction[0][1] * instruction[1],
        )
        # # print(ending_coordintate)
        # color_set[new_coordinate] = instruction[2]

        # if turn == instruction[1]:
        coordinate_set.append(new_coordinate)
        latest_coordinate = new_coordinate
    return coordinate_set


# calculates the area of a polygon
def shoelace_formula(vertices):
    n = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(n - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    sum1 = sum1 + vertices[-1][0] * vertices[0][1]
    sum2 = sum2 + vertices[0][0] * vertices[-1][1]

    area = abs(sum1 - sum2) / 2
    return area


def extract_hex(line):
    return [direction_hex[line[-1]], int(line[1:-1], 16)]


instructions = read_input(18, extract_data, False)

# part 1
start_time_1 = perf_counter()
coordinate_set = follow_dig_instructions(instructions)
steps = sum([int(instruction[1]) for instruction in instructions])
# shoelace + Pick's theorem
print(shoelace_formula(coordinate_set) + steps / 2 + 1)

end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()

hex_instructions = []
for instruction in instructions:
    hex_instructions.append(extract_hex(instruction[2]))

coordinate_hex = follow_dig_instructions(hex_instructions)
steps_hex = sum([int(instruction[1]) for instruction in hex_instructions])

# shoelace + Pick's theorem
print(shoelace_formula(coordinate_hex) + steps_hex / 2 + 1)

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
