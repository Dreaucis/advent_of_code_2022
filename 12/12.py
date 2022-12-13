"""
This code is hot garbage. I just pushed it out in a hideous state cuz I was annoyed
"""

from collections import deque
from typing import Tuple, List

from helpers import read_file_as_list

HEATMAP = read_file_as_list("./data/12.txt", list, "")

# 12.a
dyn_heatmap = [[-1 for _ in range(len(HEATMAP[0]))] for _ in range(len(HEATMAP))]
min_heap = []


def clean_elevation(elevation: str) -> str:
    return elevation.replace("S", "a").replace("E", "z")


def find_first_letter(letter: str) -> Tuple[int, int]:
    for x in range(len(HEATMAP)):
        for y in range(len(HEATMAP[0])):
            if HEATMAP[x][y] == letter:
                return x, y


def get_elevation(pos):
    return ord(HEATMAP[pos[0]][pos[1]].replace("S", "a").replace("E", "z"))


def climbable(current, _next):
    current_elevation = get_elevation(current)
    next_elevation = get_elevation(_next)
    return (next_elevation - current_elevation) <= 1


def get_neighboors(current):
    neighboors = [
        (current[0] + 1, current[1]),
        (current[0] - 1, current[1]),
        (current[0], current[1] + 1),
        (current[0], current[1] - 1),
    ]

    neighboors = [n for n in neighboors if (0 <= n[0] < len(HEATMAP) and 0 <= n[1] < len(HEATMAP[0]))]
    neighboors = [n for n in neighboors if climbable(current, n)]
    return neighboors


start = find_first_letter("S")
end = find_first_letter("E")

# 12.a
queue = deque([(start, 0)])
visited = set()
while queue:
    pos, steps = queue.popleft()
    visited.add(pos)
    if pos == end:
        print(steps)
        break
    neighboors = get_neighboors(pos)
    for neighboor in neighboors:
        if neighboor not in visited:
            visited.add(neighboor)
            queue.append((neighboor, steps + 1))


# 12.b

def find_all_letters(letter: str) -> List[Tuple[int, int]]:
    letters = []
    for x in range(len(HEATMAP)):
        for y in range(len(HEATMAP[0])):
            if get_elevation((x,y)) == ord(letter):
                letters.append((x, y))
    return letters


def bfs(start, letter):
    queue = deque([(start, [(start, 0)], 0)])
    visited = set()
    while queue:
        current, path, steps = queue.popleft()
        visited.add(current)
        if current == end:
            return path, steps
        neighboors = get_neighboors(current)
        for neighboor in neighboors:
            if neighboor not in visited:
                visited.add(neighboor)
                if get_elevation(neighboor) == ord(letter):
                    queue.append((neighboor, path + [(neighboor, steps + 1)], steps + 1))
                else:
                    queue.append((neighboor, path, steps + 1))
    return [], 0


a_positions = find_all_letters("a")
a_steps = {}
for a_pos in a_positions:
    if a_pos in a_steps:
        continue
    a_paths, tot_steps = bfs(a_pos, "a")
    for path in a_paths:
        pos, step = path
        a_steps[pos] = tot_steps - step

print(min(a_steps.values()))
