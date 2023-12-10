import math

rl_instructions = ""
network = {}

with open("input.txt", "r") as f:
    for i, line in enumerate((line.strip() for line in f.readlines())):
        if line == "":
            continue

        if i == 0:
            rl_instructions = line
            continue

        key, elements = line.split(" = ")
        elements = elements[1:-1].split(", ")

        network[key] = {"L": elements[0], "R": elements[1]}


def solution01(network, rl_instructions):
    step = 0

    node = "AAA"
    while node != "ZZZ":
        rl_instruction = rl_instructions[step % len(rl_instructions)]
        node = network[node][rl_instruction]
        step += 1
    return step


def solution02(network, rl_instructions):
    nodes = [node for node in network if node[-1] == "A"]
    nodes_dist_to_first_z = []

    for node in nodes:
        step = 0

        while node[-1] != "Z":
            rl_instruction = rl_instructions[step % len(rl_instructions)]
            node = network[node][rl_instruction]
            step += 1

        nodes_dist_to_first_z.append(step)

    return math.lcm(*nodes_dist_to_first_z)


print("—")
print(f"Solution 01: {solution01(network, rl_instructions)}")
print(f"Solution 02: {solution02(network, rl_instructions)}")
print("—")
