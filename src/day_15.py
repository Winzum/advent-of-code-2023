from utils import read_input
from time import perf_counter


def hash_alg(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def initialization_sequence(input_data):
    lenses = {}
    for command in input_data:
        if "=" in command:
            remove = False
            command = command.split("=")
            label = command[0]
            box = hash_alg(label)
            lens = int(command[1])

        else:
            remove = True
            command = command.split("-")
            label = command[0]
            box = hash_alg(label)

        if box not in lenses:
            lenses[box] = []

        if remove:
            for original in lenses[box]:
                if f"{label} " in original:
                    lenses[box].remove(original)

        else:
            if len(lenses[box]) == 0:
                lenses[box].append(f"{label} {lens}")

            else:
                new_list = [
                    f"{label} {lens}" if f"{label} " in item else item
                    for item in lenses[box]
                ]
                original_label = [item for item in lenses[box] if f"{label} " in item]
                identical = (
                    f"{label} {lens}" == original_label[0]
                    if len(original_label) > 0
                    else False
                )
                if new_list == lenses[box] and not identical:
                    lenses[box].append(f"{label} {lens}")
                else:
                    lenses[box] = new_list

    return {key: value for key, value in lenses.items() if len(value) > 0}


def calculate_focus_power(lenses_box):
    focus_power_total = 0
    for box, lenses in lenses_box.items():
        for idx, lens in enumerate(lenses):
            focus_power = 1 + box
            focus_power *= idx + 1
            focus_power *= int(lens.split()[1])
            focus_power_total += focus_power
    return focus_power_total


start_time_1 = perf_counter()
input_data = read_input(15, lambda x: x.split(","), False)[0]

# part 1
print(sum(hash_alg(x) for x in input_data))
end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()
lenses_box = initialization_sequence(input_data)
print(calculate_focus_power(lenses_box))

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
