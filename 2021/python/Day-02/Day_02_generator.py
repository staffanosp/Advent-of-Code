import time

#def input_generator():
#    with open("input.txt") as file:
#        return (action, int(v) for line in file for (action, v) in line.strip().split())


#def input_generator_2():
#    with open("input.txt","r") as file:
#        return ((action, int(v)) for action, v in (line.strip().split() for line in file))
        #while True:
        #    try:
        #        action, v = f.readline().strip().split()
        #        yield (action, int(v))
        #    except:
        #        return


def input_generator():
    with open("input.txt","r") as f:
        for action, v in (line.strip().split() for line in f):
            yield (action, int(v))


def solution01(input):
    depth, pos_horizontal = 0,0

    for action, v in input:
        if action == "forward":
            pos_horizontal += v
        elif action == "down":
            depth += v
        elif action == "up":
            depth -= v

    return depth * pos_horizontal

def solution02(input):
    depth, pos_horizontal, aim = 0,0,0

    for action, v in input:

        if action == "forward":
            pos_horizontal += v
            depth += aim * v
        elif action == "down":
            aim += v
        elif action == "up":
            aim -= v

    return depth * pos_horizontal


solution01_start_time = time.time()
solution01 = solution01(input_generator())
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution02(input_generator())
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")

