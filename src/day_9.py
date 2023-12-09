from utils import read_input, sum_array


def extract_int_list(line):
    numbers = [int(x) for x in line.split()]
    return numbers


def predict_next(numbers):
    prediction = numbers[-1]
    differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    while not all(difference == 0 for difference in differences):
        prediction += differences[-1]
        differences = [
            differences[i + 1] - differences[i] for i in range(len(differences) - 1)
        ]
    return prediction


input_series = read_input(9, extract_int_list, False)

# part 1
extrapolated_values = []
for series in input_series:
    extrapolated_values.append(predict_next(series))
print(sum_array(extrapolated_values))

# part 2
extrapolated_values_pt2 = []
for series in input_series:
    series.reverse()
    # print(predict_next(series, True))
    extrapolated_values_pt2.append(predict_next(series))
print(sum_array(extrapolated_values_pt2))
