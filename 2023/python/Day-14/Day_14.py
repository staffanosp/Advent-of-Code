import copy


with open("input.txt", "r") as f:
    input_map = [[c for c in line] for line in [line.strip() for line in f.readlines()]]


def transpose(rows):
    return list(list(row) for row in zip(*rows))


def map_to_string(input_map):
    return "".join(["".join(x) for x in input_map])


def solution01(input_map):
    input_map = copy.deepcopy(input_map)

    w = len(input_map[0])
    h = len(input_map)

    # Move the rocks
    for x in range(w):
        row = [input_map[y][x] for y in range(h)]

        did_move = True
        while did_move:
            did_move = False

            for row_x in range(1, len(row)):
                if row[row_x] == "O" and row[row_x - 1] == ".":
                    row[row_x - 1] = "O"
                    row[row_x] = "."

                    did_move = True

        # Update the map
        for y in range(h):
            input_map[y][x] = row[y]

    return sum(
        [
            len([c for c in row if c == "O"]) * (len(input_map) - i)
            for i, row in enumerate(input_map)
        ]
    )


def solution02(input_map):
    cycles_history = []
    map_to_load = {}

    input_map = copy.deepcopy(input_map)

    w = len(input_map[0])
    h = len(input_map)

    directions = ["north", "west", "south", "east"]

    cycle = 0
    repeated = False
    while not repeated:
        for direction in directions:
            # Move the rocks
            for x in range(w):
                # Transpose for west/east
                if direction in ["west", "east"]:
                    input_map = transpose(input_map)

                row = [input_map[y][x] for y in range(h)]

                # Flip the row for east/south
                if direction in ["east", "south"]:
                    row = row[::-1]

                did_move = True
                while did_move:
                    did_move = False

                    for row_x in range(1, len(row)):
                        if row[row_x] == "O" and row[row_x - 1] == ".":
                            row[row_x - 1] = "O"
                            row[row_x] = "."

                            did_move = True

                # Flip back the row for east/south
                if direction in ["east", "south"]:
                    row = row[::-1]

                # Update the map
                for y in range(h):
                    input_map[y][x] = row[y]

                # Transpose back for west/east
                if direction in ["west", "east"]:
                    input_map = transpose(input_map)

        load = sum(
            [
                len([c for c in row if c == "O"]) * (len(input_map) - i)
                for i, row in enumerate(input_map)
            ]
        )

        map_as_string = map_to_string(input_map)

        repeated = map_as_string in cycles_history

        cycles_history.append(map_as_string)
        map_to_load[map_as_string] = load

        cycle += 1

    # find the repeating pattern
    repeated_pattern = cycles_history[-1]
    repeat_start_cycle = cycles_history.index(repeated_pattern)
    repeating_sequence = cycles_history[cycles_history.index(repeated_pattern) : -1]

    return map_to_load[
        repeating_sequence[
            (1000000000 - repeat_start_cycle - 1) % len(repeating_sequence)
        ]
    ]


print("—")
print(f"Solution 01: {solution01(input_map)}")
print(f"Solution 02: {solution02(input_map)}")
print("—")
