from collections import deque

SPACE = "."
SPLITTER = "^"
START = "S"


with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


def solution01(input_data):

    splitter_count = 0

    visited = set()

    pos = (input_data[0].index(START), 0)

    w = len(input_data[0])
    h = len(input_data)

    q = deque((pos,))

    while q:
        x, y = q.pop()

        visited.add((x, y))

        next_y = y + 1

        if next_y >= h - 1:
            continue

        next_cell = input_data[next_y][x]
        if next_cell == SPLITTER:
            splitter_count += 1

            q.append((x - 1, next_y))
            q.append((x + 1, next_y))

        else:
            if not (x, next_y) in visited:
                q.append((x, next_y))

    return splitter_count


def solution02(input_data):
    h = len(input_data)
    w = len(input_data[0])

    pos = (input_data[0].index(START), 0)

    def memoize(k, f, memo):
        if not k in memo:
            memo[k] = f(k, memo)

        return memo[k]

    def dfs(pos, memo):
        x, y = pos
        if x < 0 or x >= w:
            return 0

        next_y = y + 1

        if next_y >= h - 1:
            return 1

        next_cell = input_data[next_y][x]

        if next_cell == SPLITTER:

            l = memoize((x - 1, next_y), dfs, memo)
            r = memoize((x + 1, next_y), dfs, memo)

            return l + r
        else:

            return memoize((x, next_y), dfs, memo)

    return dfs(pos, {})


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
