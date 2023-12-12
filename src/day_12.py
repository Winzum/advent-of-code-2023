from utils import read_input, sum_array
from itertools import product
import functools


def extract_data(line):
    data = line.split()
    return [data[0], [int(n) for n in data[1].split(",")]]


def calculate_permutations(pattern, broken_groups):
    amount = 0
    permutations = []
    options = {".", "#"}
    combinations = product(options, repeat=pattern.count("?"))
    combinations = ["".join(combination) for combination in combinations]
    for combination in combinations:
        permutation = pattern.replace("?", "{}").format(*combination)
        permutation_groups = [len(perm) for perm in permutation.split(".") if perm]
        if permutation_groups == broken_groups:
            amount += 1
            permutations.append(permutation)

    return {amount: permutations}


def count_permutations(pattern, broken_groups):
    # @functools.cache
    def inner_calculate_permutations(index, permutation_list):
        if index == len(pattern):
            groups = [
                len(perm) for perm in "".join(permutation_list).split(".") if perm
            ]
            return 1 if groups == broken_groups else 0

        count = 0
        if pattern[index] == "?":
            for char in {".", "#"}:
                permutation_list[index] = char
                count += inner_calculate_permutations(index + 1, permutation_list)
        else:
            permutation_list[index] = pattern[index]
            count += inner_calculate_permutations(index + 1, permutation_list)

        return count

    permutation_list = [""] * len(pattern)
    # print(permutation_list)
    total_count = inner_calculate_permutations(0, permutation_list)
    # print("Total Count:", total_count)
    return total_count


conditions = read_input(12, extract_data, True)
# print(input_data)

# part 1
arrangements = []
for condition in conditions:
    mutations = calculate_permutations(condition[0], condition[1])
    arrangements.append(mutations)
# print(arrangements)
print(sum_array([key for dictionary in arrangements for key in dictionary]))
# print(sum_array(arrangements))

# part 2
arrangements_2 = []
# print(conditions)
for condition in conditions:
    mutations = count_permutations(condition[0], condition[1])
    arrangements_2.append(mutations)
print(sum_array(arrangements_2))

# for condition in conditions:
#     print(((condition[0] + "?") * 5)[:-1], condition[1] * 5)
#     mutations = calculate_permutations(
#         ((condition[0] + "?") * 5)[:-1], condition[1] * 5
#     )
#     print(mutations)
#     arrangements_2.append(mutations)
# print(sum_array(arrangements_2))
