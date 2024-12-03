import re

with open("input.txt", "r") as f:
    input_data = f.read().strip()


def solution01(input_data):
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_data)

    acc = 0

    for instruction in instructions:
        a, b = [int(n) for n in re.findall(r"\d+", instruction)]

        acc += a * b
    return acc


def solution02(input_data):
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", input_data)

    acc = 0

    do = True
    for instruction in instructions:

        match instruction:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:  # mul
                if do:
                    a, b = [int(n) for n in re.findall(r"\d+", instruction)]
                    acc += a * b

    return acc


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
