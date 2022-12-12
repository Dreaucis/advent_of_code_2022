from typing import List

from helpers import read_file_as_list

commands = read_file_as_list("./data/9.txt", lambda x: (x.split()[0], int(x.split()[1])), "")

# 9.a
# Attempt 1: Simulate it completely
H = [0, 0]
T = [0, 0]

DIRECTIONS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

visited_locations = set(tuple(T))
for command in commands:
    direction = DIRECTIONS[command[0]]
    steps = command[1]
    for _ in range(steps):
        prev_H = list(H)
        H[0] += direction[0]
        H[1] += direction[1]

        if abs(T[0] - H[0]) > 1 or abs(T[1] - H[1]) > 1:
            T = prev_H
            visited_locations.add(tuple(T))
print(len(visited_locations))

# 9.b
# Attempt 1: Simulate it completely
NUM_KNOTS = 9
H = [0, 0]
T = [[0, 0] for _ in range(9)]


def calculate_movement(tail: List[int], head: List[int]) -> List[int]:
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    x = tail[0]
    y = tail[1]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        x += diff_x // max(abs(diff_x), 1)
        y += diff_y // max(abs(diff_y), 1)
    return [x, y]


visited_locations = set()
visited_locations.add((tuple(T[-1])))
for command in commands:
    direction = DIRECTIONS[command[0]]
    steps = command[1]
    for _ in range(steps):
        H[0] += direction[0]
        H[1] += direction[1]
        h = H
        for i in range(len(T)):
            movement = calculate_movement(T[i], h)
            if movement == T[i]:
                break
            T[i] = movement
            h = T[i]
        visited_locations.add(tuple(T[-1]))
print(len(visited_locations))
