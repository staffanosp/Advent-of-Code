import time

with open("input.txt","r") as file:
    input_list = []

    for line in (line.strip() for line in file):
        start, stop = (x for x in line.split(" -> "))
        start = tuple(int(x) for x in start.split(","))
        stop = tuple(int(x) for x in stop.split(","))
        input_list.append([start,stop])


def solution(input_lines, ignore_diagonal):
    drawn_lines = {}
    for line in input_lines:
        start, stop = line

        dir_x = -1 if start[0] > stop[0] else 1 if start[0]<stop[0] else 0
        dir_y = -1 if start[1] > stop[1] else 1 if start[1]<stop[1] else 0

        if ignore_diagonal and dir_x and dir_y:
            continue

        distance = abs(start[0] - stop[0]) or abs(start[1] - stop[1])

        for i in range(distance + 1):
            x = start[0] + dir_x * i
            y = start[1] + dir_y * i
            drawn_lines[(x,y)] = drawn_lines.get((x,y), 0) + 1

    return sum([1 for key in drawn_lines if drawn_lines[key] > 1])


solution01_start_time = time.time()
solution01 = solution(input_list, True)
solution01_total_time = time.time() - solution01_start_time
print(f"Solution 01: {solution01}, in {solution01_total_time}")

solution02_start_time = time.time()
solution02 = solution(input_list, False)
solution02_total_time = time.time() - solution02_start_time
print(f"Solution 02: {solution02}, in {solution02_total_time}")