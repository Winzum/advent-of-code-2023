from utils import read_input, sum_array
from functools import cache


def extract_data(line):
    data = line.split()
    return [data[0], tuple(map(int, data[1].split(",")))]


@cache
def count_permutations(pattern, broken_groups, group_size=0):
    # print(pattern, broken_groups, group_size, perm)
    if pattern == "":
        if (len(broken_groups) == 1 and broken_groups[0] == group_size) or (
            len(broken_groups) == 0 and group_size == 0
        ):
            return 1
        else:
            return 0

    spring = pattern[0]
    new_pattern = pattern[1:]

    if spring == ".":
        if len(broken_groups) > 0 and group_size > 0:
            if group_size == broken_groups[0]:
                new_broken_groups = broken_groups[1:]
                return count_permutations(new_pattern, new_broken_groups)
            else:
                return 0
        if len(broken_groups) == 0 and group_size > 0:
            return 0
        return count_permutations(new_pattern, broken_groups)

    if spring == "?":
        return count_permutations(
            "." + new_pattern, broken_groups, group_size
        ) + count_permutations("#" + new_pattern, broken_groups, group_size)

    if spring == "#":
        if len(broken_groups) > 0 and group_size > 0:
            if group_size > broken_groups[0]:
                # print("# too large")
                return 0
        return count_permutations(new_pattern, broken_groups, group_size=group_size + 1)


def expand_pattern(pattern, broken_groups):
    return ((pattern + "?") * 5)[:-1], broken_groups * 5


conditions = read_input(12, extract_data, False)

# part 1
arrangements = []
for condition in conditions:
    mutations = count_permutations(*condition)
    arrangements.append(mutations)
print(sum_array(arrangements))


# part 2
arrangements_2 = []
for condition in conditions:
    # mutations = count_permutations(*condition)
    mutations = count_permutations(*expand_pattern(*condition))
    arrangements_2.append(mutations)
print(sum_array(arrangements_2))
