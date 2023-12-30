with open("input.txt", "r") as f:
    input_map = [line.strip() for line in f.readlines()]


def get_start_coords(m):
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            if v == "S":
                return (x, y)


def solution(input_map):
    w = len(input_map[0])
    h = len(input_map)

    possisble_plots = {get_start_coords(input_map)}

    for _ in range(64):
        possisble_plots_post_step = set()

        while possisble_plots:
            x, y = possisble_plots.pop()

            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                x2 = x + dx
                y2 = y + dy

                if x2 not in range(w) or y2 not in range(h):
                    continue

                if input_map[y2][x2] == "#":
                    continue

                possisble_plots_post_step.add((x2, y2))

        possisble_plots = possisble_plots_post_step

    return len(possisble_plots)


print("—")
print(f"Solution 01: {solution(input_map)}")
print("—")
