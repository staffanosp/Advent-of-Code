import time

with open("input.txt","r") as f:
    input_list = [(action, int(v)) for action, v in (i.strip().split() for i in f.readlines())]


def solution01(input_list):
    depth, pos_horizontal = 0,0

    for action, v in input_list:

        if action == "forward":
            pos_horizontal += v
        elif action == "down":
            depth += v
        elif action == "up":
            depth -= v

    return depth * pos_horizontal

def solution02(input_list):
    depth, pos_horizontal, aim = 0,0,0

    for action, v in input_list:

        if action == "forward":
            pos_horizontal += v
            depth += aim * v
        elif action == "down":
            aim += v
        elif action == "up":
            aim -= v

    return depth * pos_horizontal


solution01_start_time = time.time()
solution01 = solution01(input_list)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_list)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")

