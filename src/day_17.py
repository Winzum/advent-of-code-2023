from utils import read_input
from time import perf_counter
import heapq
from copy import deepcopy


# shitzooi
def get_neighbors(grid, point, direction, maximum=0, minimum=0):
    neighbors = []
    if minimum > 0 and 0 < direction[1] < minimum:
        match direction[0]:
            case "North":
                if point[1] - 1 >= 0:
                    neighbors.append((point[0], point[1] - 1))
            case "South":
                if point[1] + 1 < len(grid):
                    neighbors.append((point[0], point[1] + 1))
            case "West":
                if point[0] - 1 >= 0:
                    neighbors.append((point[0] - 1, point[1]))
            case "East":
                if point[0] + 1 < len(grid[0]):
                    neighbors.append((point[0] + 1, point[1]))
        return neighbors
    else:
        if (
            point[0] - 1 >= 0
            and direction[0] != "East"
            and not (direction[0] == "West" and direction[1] == maximum)
        ):
            neighbors.append((point[0] - 1, point[1]))

        if (
            point[0] + 1 < len(grid[0])
            and direction[0] != "West"
            and not (direction[0] == "East" and direction[1] == maximum)
        ):
            neighbors.append((point[0] + 1, point[1]))

        if (
            point[1] - 1 >= 0
            and direction[0] != "South"
            and not (direction[0] == "North" and direction[1] == maximum)
        ):
            neighbors.append((point[0], point[1] - 1))

        if (
            point[1] + 1 < len(grid)
            and direction[0] != "North"
            and not (direction[0] == "South" and direction[1] == maximum)
        ):
            neighbors.append((point[0], point[1] + 1))

        return neighbors


def get_direction(neighbor, current_point, direction):
    new_direction = deepcopy(direction)
    if neighbor[1] < current_point[1]:
        if new_direction[0] == "North":
            new_direction = ("North", direction[1] + 1)
        else:
            new_direction = ("North", 1)

    if neighbor[1] > current_point[1]:
        if new_direction[0] == "South":
            new_direction = ("South", direction[1] + 1)
        else:
            new_direction = ("South", 1)

    if neighbor[0] < current_point[0]:
        if new_direction[0] == "West":
            new_direction = ("West", direction[1] + 1)
        else:
            new_direction = ("West", 1)

    if neighbor[0] > current_point[0]:
        if new_direction[0] == "East":
            new_direction = ("East", direction[1] + 1)
        else:
            new_direction = ("East", 1)

    return new_direction


def calculate_losses(grid, maximum=0, minimum=0):
    losses = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            losses[(x, y)] = float("inf")
    visited = set()
    pq = [(0, (0, 0), ("", 0))]

    while len(pq) > 0:
        current_loss, current_point, current_direction = heapq.heappop(pq)

        if ((current_point, current_direction)) in visited:
            continue

        visited.add((current_point, current_direction))

        neighbors = get_neighbors(
            grid, current_point, current_direction, maximum, minimum
        )

        for neighbor in neighbors:
            loss = current_loss + int(grid[neighbor[1]][neighbor[0]])
            new_direction = get_direction(neighbor, current_point, current_direction)

            if loss < losses[neighbor]:
                if minimum > 0 and neighbor == (
                    len(input_grid[0]) - 1,
                    len(input_grid) - 1,
                ):
                    if new_direction[1] >= minimum:
                        losses[neighbor] = loss
                else:
                    losses[neighbor] = loss

            heapq.heappush(pq, (loss, neighbor, new_direction))

    return losses


input_grid = read_input(17, str, False)


# part 1
start_time_1 = perf_counter()
losses = calculate_losses(input_grid, 3)

print(losses[(len(input_grid[0]) - 1, len(input_grid) - 1)])
end_time_1 = perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"The execution time is: {execution_time_1}")

# part 2
start_time_2 = perf_counter()
losses_2 = calculate_losses(input_grid, 10, 4)
print(losses_2[(len(input_grid[0]) - 1, len(input_grid) - 1)])
end_time_2 = perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"The execution time is: {execution_time_2}")
