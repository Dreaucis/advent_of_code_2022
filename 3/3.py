from functools import reduce

from helpers import read_file_as_list

rucksacks = read_file_as_list("./data/3.csv", str, "")


# 3.a

def get_prio(letter: str) -> int:
    prio = 26 if letter.isupper() else 0
    prio += ord(letter.lower()) - 96
    return prio


total_prio = 0
for rucksack in rucksacks:
    half = len(rucksack) // 2
    first_comp, second_comp = rucksack[:half], rucksack[half:]

    common = set(first_comp).intersection(set(second_comp))
    total_prio += get_prio(common.pop())

print(total_prio)

# 3.b
total_prio = 0
elf_group = []
for rucksack in rucksacks:
    elf_group.append(set(rucksack))
    if len(elf_group) < 3:
        continue
    common = reduce(lambda x, y: x.intersection(y), elf_group)
    total_prio += get_prio(common.pop())
    elf_group = []

print(total_prio)
