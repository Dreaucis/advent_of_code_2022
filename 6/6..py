from collections import Counter

from helpers import read_file_as_list

signal = read_file_as_list("./data/6.csv", str, "", "\n")[0]


def find_marker(marker_length: int, signal: str):
    marker = Counter()
    l, r = 0, 0
    while r < len(signal) - 1:
        marker = +marker
        if len(marker) == marker_length:
            break
        marker[signal[r]] += 1
        r += 1
        if r - l <= marker_length:
            continue
        marker[signal[l]] -= 1
        l += 1
    return r


# 6.a
print(find_marker(4, signal))

# 6.b
print(find_marker(14, signal))
