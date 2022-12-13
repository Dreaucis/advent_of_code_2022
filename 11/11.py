from functools import reduce
from typing import Callable, List
from collections import deque

from helpers import read_file_as_list

monkey_definitions = read_file_as_list("./data/11.txt", str, "")


# 11.a

class Monkey:
    def __init__(self, number: int, items: List[int], operation: Callable, test: Callable[[int], int], divisor: int):
        self.number = number
        self.items = deque(items)
        self.operation = operation
        self.test = test
        self.num_inspections = 0
        self.divisor = divisor


def parse_monkey(monkey: List[str]) -> Monkey:
    # Define number
    number = int(monkey[0].strip("Monkey ").strip(":"))
    # Define items
    starting_items = monkey[1].split(":")[1].split(",")
    starting_items = [int(starting_item.strip()) for starting_item in starting_items]

    # Define operation
    _op = monkey[2].split("=")[1].strip()

    def _operation(old: int):
        return eval(_op)

    # Define test
    _divisor = int(monkey[3].rsplit(" ")[-1])
    _true_monkey = int(monkey[4].rsplit(" ")[-1])
    _false_monkey = int(monkey[5].rsplit(" ")[-1])

    def _divisible_test(x: int) -> int:
        if x % _divisor == 0:
            return _true_monkey
        return _false_monkey

    return Monkey(number=number, items=starting_items, operation=_operation, test=_divisible_test, divisor=_divisor)


monkeys = {}
for i in range(len(monkey_definitions) // 7 + 1):
    monkey_definition = monkey_definitions[i * 7:(i + 1) * 7]
    monkey = parse_monkey(monkey_definition)
    monkeys[monkey.number] = monkey

for r in range(20):
    for monkey in monkeys.values():
        for _ in range(len(monkey.items)):
            item_worry = monkey.items.popleft()
            item_worry = monkey.operation(item_worry)
            item_worry = item_worry // 3
            next_monkey_number = monkey.test(item_worry)
            monkeys[next_monkey_number].items.append(item_worry)
            monkey.num_inspections += 1

print(reduce(lambda x, y: x * y, sorted([monkey.num_inspections for monkey in monkeys.values()])[-2:]))


# 11.b
monkeys = {}
for i in range(len(monkey_definitions) // 7 + 1):
    monkey_definition = monkey_definitions[i * 7:(i + 1) * 7]
    monkey = parse_monkey(monkey_definition)
    monkeys[monkey.number] = monkey

mods = [monkey.divisor for monkey in monkeys.values()]
mod_prod = reduce(lambda x, y: x * y, mods)
for r in range(10000):
    for monkey in monkeys.values():
        for _ in range(len(monkey.items)):
            item_worry = monkey.items.popleft()
            item_worry = monkey.operation(item_worry)
            item_worry = item_worry % mod_prod
            next_monkey_number = monkey.test(item_worry)
            monkeys[next_monkey_number].items.append(item_worry)
            monkey.num_inspections += 1
print(reduce(lambda x, y: x * y, sorted([monkey.num_inspections for monkey in monkeys.values()])[-2:]))