from itertools import product


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


def solution02(grid):
    w = len(grid[0])
    h = len(grid)

    start_position = None
    obstacles = set()

    # parse input
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

    loop = []

    for potential_obstacle in potential_obstacles:

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

            if ((next_x, next_y), direction) in visited:
                loop.append(potential_obstacle)
                break

            position = (next_x, next_y)

    return len(loop)


print("—")
print(f"Solution 01: {solution01(grid)}")
print(f"Solution 02: {solution02(grid)}")
print("—")
