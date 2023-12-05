from utils import read_multisection_input


def extract_seeds(section):
    seeds_list = section.split()
    return list(map(int, seeds_list[1:]))


def extract_seeds_pt2(section):
    section_list = list(map(int, section.split()[1:]))
    # print(section_list)
    seeds_list = []
    for idx, part in enumerate(section_list):
        # print(idx)
        # print(part)
        if (idx + 1) % 2 == 0:
            # print(section_list[idx - 1])
            for number in range(section_list[idx - 1], section_list[idx - 1] + part):
                seeds_list.append(number)
    return seeds_list


# destination, source, range
def extract_maps(section):
    maps_list = []
    section_list = section.splitlines()
    # drop first line
    section_list = section_list[1:]
    for section_line in section_list:
        maps_list.append(list(map(int, section_line.split())))
    return maps_list


# convert map to dict
def map_to_dict(destination, source, map_range):
    destination_list = [
        number for number in range(destination, destination + map_range)
    ]
    source_list = [number for number in range(source, source + map_range)]
    return dict(zip(source_list, destination_list))


# compile maps together
def maps_to_dict(maps_list):
    maps_dict = {}
    for map_list in maps_list:
        maps_dict.update(map_to_dict(map_list[0], map_list[1], map_list[2]))
    return dict(sorted(maps_dict.items()))


def get_key_by_value(my_dict, target_value):
    for key, value in my_dict.items():
        if value == target_value:
            return key


# create a combination of all different step maps too. Too large
def combine_maps(steps_maps):
    # steps_maps = list(reversed(steps_maps))
    final_dict = {}
    combined_dict = {}
    for idx, step_maps in enumerate(steps_maps):
        step_dict = maps_to_dict(step_maps)
        print(f"step {idx + 1}")
        # print(f"dict of step {idx + 1}: {step_dict}")
        if idx == 0:
            combined_dict.update(step_dict)
        else:
            for key, value in step_dict.items():
                if key in final_dict.values():
                    # print(final_dict)
                    # print(f"{key}->{value}")
                    # print(final_dict.values())
                    final_dict_key = get_key_by_value(final_dict, key)

                    combined_dict[final_dict_key] = value
                else:
                    combined_dict[key] = value

        final_dict.update(combined_dict)
        # print(f"final step {idx + 1}: {dict(sorted(final_dict.items()))}\n")
        # if idx == 6:
        #    quit()
    return dict(sorted(final_dict.items()))


# too large
def compare_seeds(seeds, combined_maps):
    locations = []
    for seed in seeds:
        locations.append(combined_maps[seed])
    return locations


# way easier
def seeds_search(seeds, steps_maps):
    for step_maps in steps_maps:
        print(step_maps)
        for idx, seed in enumerate(seeds):
            for step_line in step_maps:
                if seed in range(step_line[1], step_line[1] + step_line[2]):
                    seeds[idx] = seed - (step_line[1] - step_line[0])
    return seeds


transformers = [
    extract_seeds,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
]


transformers_pt2 = [
    extract_seeds_pt2,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
    extract_maps,
]

# first entry is seeds, rest are the maps
input_data = read_multisection_input(5, transformers, False)

# part 1
# combined_maps = combine_maps(input_data[1:])
# print(combine_maps)
# print(min(compare_seeds(input_data[0], combined_maps)))
seeds = seeds_search(input_data[0], input_data[1:])
print(min(seeds))

# part 2
# first entry is seeds, rest are the maps
input_data_pt2 = read_multisection_input(5, transformers_pt2, False)
# print(input_data_pt2)
# seeds_pt2 = seeds_search(input_data_pt2[0], input_data_pt2[1:])
# print(min(seeds_pt2))
