import copy

with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]


adj = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]

PAPER_ROLL = "@"


def isAccessible(pos, grid):
    w = len(grid[0])
    h = len(grid)
    x, y = pos

    adj_rolls = 0

    for dx, dy in adj:
        adj_x = x + dx
        adj_y = y + dy

        if adj_x < 0:
            continue

        if adj_x > w - 1:
            continue

        if adj_y < 0:
            continue

        if adj_y > h - 1:
            continue

        if grid[adj_y][adj_x] == PAPER_ROLL:
            adj_rolls += 1

        if adj_rolls >= 4:
            return False

    return True


def solution01(grid):
    grid = copy.deepcopy(grid)

    w = len(grid[0])
    h = len(grid)

    rolls = 0

    for x in range(w):
        for y in range(h):
            if grid[y][x] != PAPER_ROLL:
                continue

            if isAccessible((x, y), grid):
                rolls += 1

    return rolls


def solution02(grid):
    grid = copy.deepcopy(grid)

    w = len(grid[0])
    h = len(grid)

    rolls = 0
    changed = True

    while changed:
        changed = False

        for x in range(w):
            for y in range(h):
                if grid[y][x] != PAPER_ROLL:
                    continue

                if isAccessible((x, y), grid):
                    grid[y][x] = "."
                    rolls += 1
                    changed = True

    return rolls


print("—")
print(f"Solution 01: {solution01(grid)}")
print(f"Solution 02: {solution02(grid)}")
print("—")
