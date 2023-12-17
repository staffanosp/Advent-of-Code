from collections import deque


with open("input.txt", "r") as f:
    input_map = [[c for c in line] for line in [line.strip() for line in f.readlines()]]


def solution(input_map, part):
    w = len(input_map[0])
    h = len(input_map)

    # Part 1 / 2 setup
    if part == 1:
        start_beams = [(-1, 0, 1, 0)]
    else:
        start_beams = []
        for y in range(h):
            for x, dx in [(-1, 1), (w, -1)]:
                start_beams.append((x, y, dx, 0))

        for x in range(w):
            for y, dy in [(-1, 1), (h, -1)]:
                start_beams.append((x, y, 0, dy))

    # Solution
    energized_tiles_sums = []

    for start_beam in start_beams:
        beams = deque([start_beam])

        energized_tiles = set()
        prev_beam_states = set()

        while beams:
            beam = beams.popleft()

            if beam in prev_beam_states:
                continue

            prev_beam_states.add(beam)

            x, y, dx, dy = beam
            x += dx
            y += dy

            if (not 0 <= x <= w - 1) or (not 0 <= y <= h - 1):
                continue

            energized_tiles.add((x, y))

            match input_map[y][x]:
                case ".":
                    beams.append((x, y, dx, dy))
                case "|":
                    if dx:
                        beams.append((x, y, 0, -1))
                        beams.append((x, y, 0, 1))
                    else:
                        beams.append((x, y, dx, dy))
                case "-":
                    if dy:
                        beams.append((x, y, -1, 0))
                        beams.append((x, y, 1, 0))
                    else:
                        beams.append((x, y, dx, dy))
                case "/":
                    if dx:
                        beams.append((x, y, 0, -dx))
                    else:
                        beams.append((x, y, -dy, 0))
                case "\\":
                    if dx:
                        beams.append((x, y, 0, dx))
                    else:
                        beams.append((x, y, dy, 0))

        energized_tiles_sums.append(len(energized_tiles))

    return max(energized_tiles_sums)


print("—")
print(f"Solution 01: {solution(input_map,1)}")
print(f"Solution 02: {solution(input_map,2)}")
print("—")
