from itertools import combinations

galaxies = []

with open("input.txt", "r") as f:
    for y, line in enumerate([line.strip() for line in f.readlines()]):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))


def solution(galaxies, expansion_multiplier):
    empty_cols = [
        x
        for x in range(max([x for x, _ in galaxies]) + 1)
        if not x in [x for x, _ in galaxies]
    ]

    empty_rows = [
        y
        for y in range(max([y for _, y in galaxies]) + 1)
        if not y in [y for _, y in galaxies]
    ]

    galaxies_expanded = []
    for x, y in galaxies:
        x_expanded = x
        y_expanded = y

        for col in empty_cols:
            if x > col:
                x_expanded += expansion_multiplier - 1
            else:
                break

        for row in empty_rows:
            if y > row:
                y_expanded += expansion_multiplier - 1
            else:
                break

        galaxies_expanded.append((x_expanded, y_expanded))

    return sum(
        [
            abs(x1 - x2) + abs(y1 - y2)
            for [(x1, y1), (x2, y2)] in combinations(galaxies_expanded, 2)
        ]
    )


print("—")
print(f"Solution 01: {solution(galaxies, 2)}")
print(f"Solution 02: {solution(galaxies, 1_000_000)}")
print("—")
