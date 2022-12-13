from functools import cmp_to_key, reduce
from typing import Union

from helpers import read_file_as_list

raw_comparisons = read_file_as_list("./data/13.txt", str, "")

comparisons = list(filter(lambda x: x, raw_comparisons))
comparison_pairs = [(eval(comparisons[2 * i]), eval(comparisons[2 * i + 1])) for i in range(len(comparisons) // 2)]


def is_correct_order(left: Union[list, int], right: Union[list, int]) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        return left <= right

    if isinstance(left, list) and isinstance(right, list):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            left_leq = is_correct_order(left[i], right[i])
            right_leq = is_correct_order(right[i], left[i])
            if left_leq and right_leq:
                continue
            return left_leq
        if len(left) > len(right):
            return False
        return True

    if isinstance(left, int) and isinstance(right, list):
        return is_correct_order([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return is_correct_order(left, [right])

    raise ValueError


# 13.a
index = 1
correct_order_index = []
for pair in comparison_pairs:
    left, right = pair
    print(left)
    print(right)
    if is_correct_order(left, right):
        correct_order_index.append(index)
        print("TRUE")
    index += 1
    print("---")
print(sum(correct_order_index))

# 13.b
DIVIDER_PACKETS = ([[2]], [[6]])

all_packets = []
for pair in comparison_pairs:
    all_packets.extend(pair)
all_packets.extend(DIVIDER_PACKETS)


def compare(left: Union[list, int], right: Union[list, int]) -> int:
    if left == right:
        return 0
    return 2 * int(is_correct_order(left, right)) - 1


sorted_packets = sorted(all_packets, key=cmp_to_key(compare), reverse=True)
print(reduce(lambda x, y: x * y, (sorted_packets.index(x) + 1 for x in DIVIDER_PACKETS)))
