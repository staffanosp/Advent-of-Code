with open("input.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]


PIPE_CONNECTIONS = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
    ".": [],
    "S": ["north", "east", "south", "west"],
}

COMPATIBLE_CONNECTIONS = {
    "west": "east",
    "east": "west",
    "north": "south",
    "south": "north",
}

DIRECTION_TO_COORDS = {
    "north": (0, -1),
    "east": (1, 0),
    "south": (0, 1),
    "west": (-1, 0),
}


def get_start_coords(grid):
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            if v == "S":
                return x, y


def solution(grid):
    x, y = get_start_coords(grid)

    visited_coords = []
    start_used_connection = None

    step = 0
    while grid[y][x] != "S" or step == 0:
        if step > 0:
            visited_coords.append((x, y))

        curr_pipe = grid[y][x]

        for direction in PIPE_CONNECTIONS[curr_pipe]:
            check_x = x + DIRECTION_TO_COORDS[direction][0]
            check_y = y + DIRECTION_TO_COORDS[direction][1]

            if (check_x, check_y) in visited_coords:
                continue

            check_pipe = grid[check_y][check_x]

            required_connection = COMPATIBLE_CONNECTIONS[direction]

            check_pipe_connections = PIPE_CONNECTIONS[check_pipe]

            # remove the "used" connection from S
            if check_pipe == "S":
                check_pipe_connections = [
                    connection
                    for connection in check_pipe_connections
                    if connection != start_used_connection
                ]

            if required_connection in check_pipe_connections:
                # move
                x = check_x
                y = check_y

                # keep track of S' "used" connection
                if curr_pipe == "S":
                    start_used_connection = direction
                break

        step += 1

    return step // 2


print("—")
print(f"Solution 01: {solution(grid)}")
# print(f"Solution 02: {solution(input_data)}")
print("—")
