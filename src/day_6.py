from utils import read_input
from math import sqrt, floor
import numpy as np


# back to school
# distance = (race_time - hold_time ) * hold_time
# distance = (race_time * hold_time) - hold_time ** 2
# 0 =  -hold_time ** 2 + (race_time * hold_time) - distance
# 0 = -x**                 + ax                 - c


def quadratic_formula(a, b, c):
    delta = sqrt(b**2 - 4 * a * c)
    root_1 = (-b + delta) / (2 * a)
    root_2 = (-b - delta) / (2 * a)
    return root_1, root_2


def extract_data(line):
    line_values = line.split()[1:]
    return [int(value) for value in line_values]


def extract_data_pt2(line):
    line_values = line.split()[1:]
    return [int("".join(line_values))]


def multiply_race_records(race_dict):
    records = []
    for key, value in race_dict.items():
        root_1, root_2 = quadratic_formula(-1, key, -value)
        if root_2 == int(root_2):
            root_2 = root_2 - 1
        records.append(floor(root_2) - floor(root_1))
    # print(records)
    return np.prod(records)


# part 1
race_data = read_input(6, extract_data, False)
# print(race_data)
race_dict = dict(zip(race_data[0], race_data[1]))
print(multiply_race_records(race_dict))

# part 2
race_data_pt2 = read_input(6, extract_data_pt2, False)
race_dict_pt2 = dict(zip(race_data_pt2[0], race_data_pt2[1]))
print(multiply_race_records(race_dict_pt2))
