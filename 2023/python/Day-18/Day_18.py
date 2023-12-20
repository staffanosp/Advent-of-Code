from collections import deque

with open("input.txt", "r") as f:
    dig_plan = [
        (direction, int(length), color[1:-1])
        for direction, length, color in [
            line.strip().split(" ") for line in f.readlines()
        ]
    ]


DIRECTION_TO_COORDS = {
    "U": (0, -1),
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
}


def solution(dig_plan):
    x = 0
    y = 0

    # get the outline
    outline_map = {(0, 0)}
    for direction, length, _ in dig_plan:
        dx, dy = DIRECTION_TO_COORDS[direction]

        for i in range(length):
            x += dx
            y += dy
            outline_map.add((x, y))

    # get bounding box
    l = min([x for x, _ in outline_map]) - 1
    r = max([x for x, _ in outline_map]) + 1
    t = min([y for _, y in outline_map]) - 1
    b = max([y for _, y in outline_map]) + 1

    # fill
    fill_map = set()

    queue = deque()

    queue.append((l, t))

    while queue:
        x, y = queue.popleft()

        if (x, y) in fill_map:
            continue

        if (x, y) in outline_map:
            continue

        if x not in range(l, r + 1) or y not in range(t, b + 1):
            continue

        fill_map.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            queue.append((x + dx, y + dy))

    return (r - l + 1) * (b - t + 1) - len(fill_map)


print("—")
print(f"Solution 01: {solution(dig_plan)}")
print("—")
