from collections import deque

from helpers import read_file_as_list

assignments = read_file_as_list("./data/5.csv", str, "", "\n")

# 5.a
empty_line = assignments.index("")
cargo_lines = assignments[:empty_line - 1]
command_lines = assignments[empty_line + 1:]

num_stacks = (len(cargo_lines[0]) + 1) // 4
cargo_stacks = [deque() for i in range(num_stacks)]
cargo_indexes = [1 + 4 * x for x in range(num_stacks)]
for cargo_line in cargo_lines:
    cargos = [cargo_line[cargo_index] for cargo_index in cargo_indexes]
    for i, cargo in enumerate(cargos):
        if cargo == " ":
            continue
        cargo_stacks[i].append(cargo)

for command in command_lines:
    command_list = command.split()
    amount, from_stack_id, to_stack_id = int(command_list[1]), int(command_list[3]) - 1, int(command_list[5]) - 1
    for _ in range(amount):
        cargo_to_move = cargo_stacks[from_stack_id].popleft()
        cargo_stacks[to_stack_id].appendleft(cargo_to_move)

top_cargo = "".join([cargo_stack.popleft() for cargo_stack in cargo_stacks])
print(top_cargo)

# 5.b
empty_line = assignments.index("")
cargo_lines = assignments[:empty_line - 1]
command_lines = assignments[empty_line + 1:]

num_stacks = (len(cargo_lines[0]) + 1) // 4
cargo_stacks = [deque() for i in range(num_stacks)]
cargo_indexes = [1 + 4 * x for x in range(num_stacks)]
for cargo_line in cargo_lines:
    cargos = [cargo_line[cargo_index] for cargo_index in cargo_indexes]
    for i, cargo in enumerate(cargos):
        if cargo == " ":
            continue
        cargo_stacks[i].append(cargo)

for command in command_lines:
    command_list = command.split()
    amount, from_stack_id, to_stack_id = int(command_list[1]), int(command_list[3]) - 1, int(command_list[5]) - 1
    cargo_to_move = deque()
    for _ in range(amount):
        cargo_to_move.appendleft(cargo_stacks[from_stack_id].popleft())

    cargo_stacks[to_stack_id].extendleft(cargo_to_move)

top_cargo = "".join([cargo_stack.popleft() for cargo_stack in cargo_stacks])
print(top_cargo)
