from typing import List

from helpers import read_file_as_list

assignments = read_file_as_list("./data/4.csv", lambda x: x.split(","), "")


# 4.a
def str_range_to_int(str_range: str) -> List[int]:
    return [int(x) for x in str_range.split("-")]


def is_enveloped(range1: List[int], range2: List[int]) -> bool:
    if range1[0] >= range2[0] and range1[-1] <= range2[-1]:
        return True
    return False


num_envelops = 0
for first_range, second_range in assignments:
    first_range = str_range_to_int(first_range)
    second_range = str_range_to_int(second_range)
    if is_enveloped(first_range, second_range) or is_enveloped(second_range, first_range):
        num_envelops += 1
print(num_envelops)


# 4.b
def is_overlapping(range1: List[int], range2: List[int]) -> bool:
    if range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]:
        return True
    return False

num_overlaps = 0
for first_range, second_range in assignments:
    first_range = str_range_to_int(first_range)
    second_range = str_range_to_int(second_range)
    if is_overlapping(first_range, second_range) or is_enveloped(second_range, first_range):
        num_overlaps += 1
print(num_overlaps)
