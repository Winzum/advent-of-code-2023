from utils import read_multisection_input
import math


def extract_instructions(section):
    return [step for step in section]


def extract_nodes(section):
    nodes = dict()
    for node in section.splitlines():
        split_node = node.split("=")
        location_split = split_node[1].split(",")
        nodes[split_node[0].strip()] = [
            location_split[0].strip()[1:],
            location_split[1].strip()[:-1],
        ]

    return nodes


def search(instructions, nodes):
    found = False
    steps = 0
    current_location = "AAA"
    while not found:
        for instruction in instructions:
            if current_location == "ZZZ":
                found = True
                return steps
            if instruction == "L":
                current_location = nodes[current_location][0]
            elif instruction == "R":
                current_location = nodes[current_location][1]
            steps += 1


def ghost_search_multiples(instructions, nodes):
    multiples = []
    starting_locations = [key for key in nodes.keys() if key[-1] == "A"]
    for location in starting_locations:
        steps = 0
        found = False
        while not found:
            for instruction in instructions:
                if location[-1] == "Z":
                    multiples.append(steps)
                    found = True
                    break
                if instruction == "L":
                    location = nodes[location][0]
                elif instruction == "R":
                    location = nodes[location][1]
                steps += 1
    return multiples


input_data = read_multisection_input(8, [extract_instructions, extract_nodes], False)
print(input_data)

# part 1
print(search(input_data[0], input_data[1]))

# part 2
multiples = ghost_search_multiples(input_data[0], input_data[1])
# assuming lcm works
print(math.lcm(*multiples))
# print(ghost_search(input_data[0], input_data[1]))
