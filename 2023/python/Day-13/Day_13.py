import copy

patterns = []

with open("input.txt", "r") as f:
    pattern = []
    for line in [line.strip() for line in f.readlines()]:
        if line == "":
            patterns.append(pattern)
            pattern = []
            continue

        pattern.append(list(line))

    patterns.append(pattern)


def gen_smudge_patterns(pattern):
    h = len(pattern)
    w = len(pattern[0])

    for y in range(h):
        for x in range(w):
            smudge_pattern = copy.deepcopy(pattern)
            char = smudge_pattern[y][x]
            smudge_pattern[y][x] = "." if char == "#" else "#"
            yield smudge_pattern


def solution01(patterns):
    patterns = copy.deepcopy(patterns)

    splits = {}

    for rows_or_cols in ["rows", "cols"]:
        for pattern_i, pattern in enumerate(patterns):
            if pattern_i in splits:
                continue

            if rows_or_cols == "cols":
                pattern = [list(row) for row in zip(*pattern)]

            h = len(pattern)

            for split_i in range(1, h):
                a = pattern[:split_i][::-1]
                b = pattern[split_i:]

                min_a_b = min(len(a), len(b))

                is_reflection = tuple(a[:min_a_b]) == tuple(b[:min_a_b])

                if is_reflection:
                    splits[pattern_i] = (split_i, rows_or_cols)
                    break

    # Sum it all up
    sums = {"rows": 0, "cols": 0}
    for split_i, rows_or_cols in splits.values():
        sums[rows_or_cols] += split_i

    return sums["cols"] + sums["rows"] * 100


def solution02(patterns):
    patterns = copy.deepcopy(patterns)

    # Save splits for original patterns (this is basically just copy paste of part 1...)
    original_splits = {}

    for rows_or_cols in ["rows", "cols"]:
        for pattern_i, pattern in enumerate(patterns):
            if pattern_i in original_splits:
                continue

            if rows_or_cols == "cols":
                pattern = [list(row) for row in zip(*pattern)]

            h = len(pattern)

            for split_i in range(1, h):
                a = pattern[:split_i][::-1]
                b = pattern[split_i:]

                min_a_b = min(len(a), len(b))

                is_reflection = tuple(a[:min_a_b]) == tuple(b[:min_a_b])

                if is_reflection:
                    original_splits[pattern_i] = (split_i, rows_or_cols)
                    break

    # Smudge fix. This is really where part 2 begins.
    smudge_fixed_splits = {}

    for rows_or_cols in ["rows", "cols"]:
        for pattern_i, pattern in enumerate(patterns):
            if pattern_i in smudge_fixed_splits:
                continue

            if rows_or_cols == "cols":
                pattern = [list(row) for row in zip(*pattern)]

            h = len(pattern)

            for smudge_pattern in gen_smudge_patterns(pattern):
                for split_i in range(1, h):
                    a = smudge_pattern[:split_i][::-1]
                    b = smudge_pattern[split_i:]

                    min_a_b = min(len(a), len(b))

                    is_reflection = tuple(a[:min_a_b]) == tuple(b[:min_a_b])

                    is_new_split = is_reflection and original_splits[pattern_i] != (
                        split_i,
                        rows_or_cols,
                    )

                    if is_new_split:
                        smudge_fixed_splits[pattern_i] = (split_i, rows_or_cols)
                        break

                if is_new_split:
                    break

    # Sum it all up
    sums = {"rows": 0, "cols": 0}
    for split_i, rows_or_cols in smudge_fixed_splits.values():
        sums[rows_or_cols] += split_i

    return sums["cols"] + sums["rows"] * 100


print("—")
print(f"Solution 01: {solution01(patterns)}")
print(f"Solution 02: {solution02(patterns)}")
print("—")
