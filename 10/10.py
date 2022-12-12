from helpers import read_file_as_list

instructions = read_file_as_list("./data/10.txt", str, "")

# 10.a
def noop(val: int):
    yield val


def addx(arg: str):
    arg = int(arg)
    def _addx(val: int):
        n_cycles = 2
        for i in range(n_cycles):
            yield val if i < n_cycles - 1 else val + arg

    return _addx

commands = {
    "noop": noop,
    "addx": addx
}

signal_strength_cycles = [20 + 40*i for i in range(6)]
signal_strength_sum = 0

cycle = 1
x = 1
for instruction in instructions:
    ins = instruction.split()
    if len(ins) > 1:
        command = commands[ins[0]](ins[1])
    else:
        command = commands[ins[0]]

    for val in command(x):
        cycle += 1
        x = val
        if cycle in signal_strength_cycles:
            signal_strength_sum += cycle * x

print(signal_strength_sum)

# 10.b
CRT_WIDTH = 40
CRT_HEIGHT = 6
SPRITE_WIDTH = 3

pixels = []
cycle = 1
x = 1
max_x = 0
for instruction in instructions:
    ins = instruction.split()
    if len(ins) > 1:
        command = commands[ins[0]](ins[1])
    else:
        command = commands[ins[0]]

    sprite_pos = [(x+i) for i in range(SPRITE_WIDTH)]
    for val in command(x):
        if ((cycle - 1) % CRT_WIDTH + 1) in sprite_pos:
            pixels.append("#")
        else:
            pixels.append(".")
        cycle += 1
        x = val
        max_x = max(x, max_x)
print(max_x)
for h in range(CRT_HEIGHT):
    print("".join(pixels[h*CRT_WIDTH:(h+1)*CRT_WIDTH]))