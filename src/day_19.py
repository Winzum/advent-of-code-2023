from utils import read_multisection_input
from time import perf_counter
from pprint import pprint


def extract_workflow(section):
    workflows = {}
    for line in section.split("\n"):
        name = line[: line.find("{")]
        workflows[name] = [x.split(":") for x in line.split(name)[1][1:-1].split(",")]
    return workflows


def extract_xmas(section):
    parts_list = []
    for line in section.split("\n"):
        part_dict = {}
        parts = line[1:-1].split(",")
        # print(parts)
        for part in parts:
            part_dict[part[0]] = int(part[2:])
        parts_list.append(part_dict)
    return parts_list


def evaluate_part(part, workflows):
    # print(part)
    result = ""
    workflow = workflows["in"]
    while result not in ("R", "A"):
        for rule in workflow:
            if rule == workflow[-1]:
                result = rule[0]
            else:
                # print(eval(rule[0], globals(), part))
                if eval(rule[0], globals(), part):
                    result = rule[1]
                    break
        if result not in ("R", "A"):
            workflow = workflows[result]
    return result


input_data = read_multisection_input(19, [extract_workflow, extract_xmas], False)
# print(input_data)

# part 1
start_time_1 = perf_counter()
workflows, parts = input_data[0], input_data[1]
# pprint(workflows)
worth = 0
for part in parts:
    if evaluate_part(part, workflows) == "A":
        worth += sum(part.values())
print(worth)

end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()

end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
