from itertools import product

with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]


def is_within_range(pos, w, h):
    x, y = pos

    if x not in range(w):
        return False

    if y not in range(h):
        return False

    return True


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def get_regions(grid):
    w = len(grid[0])
    h = len(grid)

    checked = set()
    regions = []

    for x, y in product(range(w), range(h)):
        if (x, y) in checked:
            continue

        region_name = grid[y][x]
        region = {(x, y)}

        q = [(x, y)]

        while q:
            x, y = q.pop()

            for x2, y2 in [(dx + x, dy + y) for dx, dy in DIRECTIONS]:
                if not is_within_range((x2, y2), w, h):
                    continue

                if not grid[y2][x2] == region_name:
                    continue

                if not (x2, y2) in region:
                    q.append((x2, y2))
                    region.add((x2, y2))

        regions.append(region)
        checked.update(region)

    return regions


def get_corners(pos, region, w, h):

    x, y = pos

    corners = 0

    for i, (dx, dy) in enumerate(DIRECTIONS):
        x2 = x + dx
        y2 = y + dy

        # next direction
        next_dx, next_dy = DIRECTIONS[(i + 1) % len(DIRECTIONS)]
        x3 = x + next_dx
        y3 = y + next_dy

        # diagonal
        diag_dx = dx + next_dx
        diag_dy = dy + next_dy

        diag_x = x + diag_dx
        diag_y = y + diag_dy

        if not (x2, y2) in region and not (x3, y3) in region:
            corners += 1
            continue

        if (x2, y2) in region and (x3, y3) in region and not (diag_x, diag_y) in region:
            corners += 1
            continue

    return corners


def solution01(grid):
    w = len(grid[0])
    h = len(grid)

    regions = get_regions(grid)

    price = 0
    for region in regions:
        area = len(region)

        perimeter = 0
        for x, y in region:
            for x2, y2 in [(dx + x, dy + y) for dx, dy in DIRECTIONS]:
                if not is_within_range((x2, y2), w, h):
                    perimeter += 1
                    continue

                if not (x2, y2) in region:
                    perimeter += 1
                    continue

        price += area * perimeter

    return price


def solution02(grid):
    w = len(grid[0])
    h = len(grid)

    regions = get_regions(grid)

    price = 0

    for region in regions:
        area = len(region)

        corners = 0
        for x, y in region:
            corners += get_corners((x, y), region, w, h)

        price += area * corners

    return price


print("—")
print(f"Solution 01: {solution01(grid)}")
print(f"Solution 02: {solution02(grid)}")
print("—")
