from itertools import product
from multiprocessing import Pool, cpu_count

with open("input.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]


directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def solution01(grid):
    w = len(grid[0])
    h = len(grid)

    direction = 0

    position = None
    obstacles = set()

    for x, y in product(range(w), range(h)):
        match grid[y][x]:
            case "#":
                obstacles.add((x, y))
            case "^":
                position = (x, y)

    visited = set()

    while position[0] in range(w) and position[1] in range(h):
        visited.add(position)

        curr_x, curr_y = position
        dx, dy = directions[direction]
        next_x = curr_x + dx
        next_y = curr_y + dy

        if (next_x, next_y) in obstacles:
            direction = (direction + 1) % len(directions)
            continue

        position = (next_x, next_y)

    return len(visited)


def check_for_loop(args):
    potential_obstacle, obstacles, start_position, w, h = args

    curr_obstacles = obstacles | {potential_obstacle}

    position = start_position
    direction = 0

    visited = set()

    while position[0] in range(w) and position[1] in range(h):
        visited.add((position, direction))

        curr_x, curr_y = position
        dx, dy = directions[direction]
        next_x = curr_x + dx
        next_y = curr_y + dy

        if (next_x, next_y) in curr_obstacles:
            direction = (direction + 1) % len(directions)
            continue

        if ((next_x, next_y), direction) in visited:  # loop
            return True

        position = (next_x, next_y)

    return False


def solution02(grid):
    w = len(grid[0])
    h = len(grid)

    start_position = None
    obstacles = set()

    for x, y in product(range(w), range(h)):
        match grid[y][x]:
            case "#":
                obstacles.add((x, y))
            case "^":
                start_position = (x, y)

    potential_obstacles = [
        (x, y)
        for x, y in product(range(w), range(h))
        if not (x, y) in obstacles and not (x, y) == start_position
    ]

    args = [
        [potential_obstacle, obstacles, start_position, w, h]
        for potential_obstacle in potential_obstacles
    ]

    pools_count = cpu_count()
    with Pool(processes=pools_count) as pool:
        return sum([1 for loop in pool.map(check_for_loop, args) if loop])


if __name__ == "__main__":
    print("—")
    print(f"Solution 01: {solution01(grid)}")
    print(f"Solution 02: {solution02(grid)}")
    print("—")
