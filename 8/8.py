from typing import List

from helpers import read_file_as_list

trees = read_file_as_list("./data/8.txt", lambda x: [int(y) for y in x], "")


# 8.a
def transpose(mat: List[List[int]]) -> List[List[int]]:
    return [list(x) for x in zip(*mat)][::-1]


def count_visible_from_left(mat: List[List[int]]) -> int:
    num_visible = 0
    for i, row in enumerate(mat):
        curr_max_val = -1
        for j, val in enumerate(row):
            if val <= curr_max_val:
                continue
            curr_max_val = val
            if not isinstance(val, float):  # Has not been visited before (zero's cant be negative..
                num_visible += 1
                mat[i][j] = float(val)
    return num_visible


total_visible = count_visible_from_left(trees)
for _ in range(3):
    trees = transpose(trees)
    total_visible += count_visible_from_left(trees)
print(total_visible)

# 8.b
trees = read_file_as_list("./data/8.txt", lambda x: [int(y) for y in x], "")


def mark_visible_from_left(mat: List[List[int]], scenic_matrix: List[List[int]]) -> List[List[int]]:
    for i, row in enumerate(mat):
        latest_height_ind = {}
        for j, val in enumerate(row):
            # Find how index of the latest height that is the same or lower
            latest_geq = max(latest_height_ind.get(k, 0) for k in range(val, 10))

            scenic_matrix[i][j] *= (j - latest_geq)
            # Update index of latest height
            latest_height_ind[val] = j
    return scenic_matrix


scenic_scores = [[1] * len(row) for row in trees]
scenic_scores = mark_visible_from_left(trees, scenic_scores)
for _ in range(3):
    trees = transpose(trees)
    scenic_scores = transpose(scenic_scores)
    scenic_scores = mark_visible_from_left(trees, scenic_scores)
print(max(max(x) for x in scenic_scores))