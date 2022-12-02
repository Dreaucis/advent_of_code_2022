import heapq

from helpers import read_file_as_list

DATA_FILEPATH = "./data/1.csv"

calories = read_file_as_list(DATA_FILEPATH, int, 0)

# 1.a O(N), O(1)
curr_calories = 0
max_calories = 0
for calorie in calories:
    if calorie != 0:
        curr_calories += calorie
        continue
    if curr_calories > max_calories:
        max_calories = curr_calories
    curr_calories = 0

print(max_calories)

# 1.b O(N), O(1)
heap = [0]
curr_calories = 0
for calorie in calories:
    if calorie != 0:
        curr_calories += calorie
        continue
    if curr_calories > heap[0]:
        if len(heap) > 2:
            heapq.heappop(heap)
        heapq.heappush(heap, curr_calories)
    curr_calories = 0

print(sum(heap))
