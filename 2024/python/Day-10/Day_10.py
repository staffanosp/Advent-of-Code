from itertools import product

with open("input.txt", "r") as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def solution(grid, part):

    w = len(grid[0])
    h = len(grid)

    def find_nines(start_pos):

        nines = []

        def find_path(start_pos):
            x, y = start_pos

            if grid[y][x] == 9:
                nines.append((x, y))

            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy

                if not next_x in range(w):
                    continue
                if not next_y in range(h):
                    continue

                v = grid[y][x]
                next_v = grid[next_y][next_x]

                if next_v == v + 1:
                    find_path((next_x, next_y))

        find_path(start_pos)

        return nines

    trailheads = []
    for x, y in product(range(w), range(h)):
        if grid[y][x] == 0:
            trailheads.append((x, y))

    match part:
        case 1:
            return sum([len(set(find_nines(trailhead))) for trailhead in trailheads])
        case 2:
            return sum([len(find_nines(trailhead)) for trailhead in trailheads])


print("—")
print(f"Solution 01: {solution(grid,1)}")
print(f"Solution 02: {solution(grid,2)}")
print("—")
