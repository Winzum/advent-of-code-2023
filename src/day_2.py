from utils import read_input, sum_array
import re


def extract_game(line):
    game_pattern = re.compile(r"Game (\d+):")
    return game_pattern.findall(line)[0]


def extract_cubes(line):
    cube_pattern = re.compile(r"(\d+) (\w+)")
    cube_matches = cube_pattern.findall(line)
    return cube_matches


def compare_cubes_with_dict(cube_list, cube_dict):
    for amount, color in cube_list:
        if cube_dict[color] < int(amount):
            return False
    return True


def extract_hightest_cube_product(cube_list):
    highest_cubes = {"red": 0, "green": 0, "blue": 0}
    for amount, color in cube_list:
        amount = int(amount)
        highest_cubes[color] = max(amount, highest_cubes[color])
    return highest_cubes["red"] * highest_cubes["green"] * highest_cubes["blue"]


def extract_data(line):
    return [int(extract_game(line)), extract_cubes(line)]


games = read_input(2, extract_data, False)

# part 1
cube_dict = {"red": 12, "green": 13, "blue": 14}
print(sum(game[0] for game in games if compare_cubes_with_dict(game[1], cube_dict)))

# part 2
print(sum_array([extract_hightest_cube_product(game[1]) for game in games]))
