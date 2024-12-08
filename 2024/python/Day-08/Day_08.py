from collections import defaultdict
from itertools import combinations

all_antennas = defaultdict(list)
w = None
h = None

with open("input.txt", "r") as f:

    for y, line in enumerate([line.strip() for line in f.readlines()]):
        for x, v in enumerate(line):
            if v == ".":
                continue

            all_antennas[v].append((x, y))

    w = x
    h = y


def solution01(all_antennas, w, h):

    antinodes = set()

    for antennas in all_antennas.values():
        antenna_pairs = list(combinations(antennas, 2))

        for antenna_pair in antenna_pairs:
            a, b = antenna_pair
            (ax, ay), (bx, by) = a, b

            dx = ax - bx
            dy = ay - by

            potential_antinodes = [
                (ax + dx, ay + dy),
                (bx - dx, by - dy),
            ]

            for antinode_x, antinode_y in potential_antinodes:
                if not antinode_x in range(w + 1):
                    continue
                if not antinode_y in range(h + 1):
                    continue

                antinodes.add((antinode_x, antinode_y))

    return len(antinodes)


def solution02(all_antennas, w, h):

    antinodes = set()

    for antennas in all_antennas.values():
        antenna_pairs = list(combinations(antennas, 2))

        for antenna_pair in antenna_pairs:
            a, b = antenna_pair
            (ax, ay), (bx, by) = a, b

            dx = ax - bx
            dy = ay - by

            for direction in ["+", "-"]:

                i = 0
                while True:
                    match direction:
                        case "+":
                            antinode = (ax + dx * i, ay + dy * i)
                        case "-":
                            antinode = (bx - dx * i, by - dy * i)

                    antinode_x, antinode_y = antinode

                    if not antinode_x in range(w + 1):
                        break
                    if not antinode_y in range(h + 1):
                        break

                    antinodes.add(antinode)
                    i += 1

    return len(antinodes)


print("—")
print(f"Solution 01: {solution01(all_antennas,w,h)}")
print(f"Solution 02: {solution02(all_antennas,w,h)}")
print("—")
