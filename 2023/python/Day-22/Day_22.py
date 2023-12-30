from functools import cmp_to_key


with open("input.txt", "r") as f:
    input_blocks = [
        (tuple(int(n) for n in start.split(",")), tuple(int(n) for n in end.split(",")))
        for line in (line.strip() for line in f.readlines())
        for start, end in [line.split("~")]
    ]


def sort_by_z(a, b):
    a_z = min(a[0][2], a[1][2])
    b_z = min(b[0][2], b[1][2])

    if a_z > b_z:
        return 1
    elif a_z < b_z:
        return -1
    else:
        return 0


def settle_blocks(blocks, disintegrated_block=None):
    settled_blocks = []

    # create x y map to keep track of max z values
    max_x = max(max(x1, x2) for _, (x1, _, _), (x2, _, _) in blocks)
    max_y = max(max(y1, y2) for _, (_, y1, _), (_, y2, _) in blocks)

    height_map = [[0 for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1)]

    for block in blocks:
        if block == disintegrated_block:
            continue

        block_id, (x1, y1, z1), (x2, y2, z2) = block

        # first block always goes straight to floor
        if not settled_blocks:
            settled_blocks.append((block_id, (x1, y1, 1), (x2, y2, z2 - (z1 - 1))))
            update_height_map(height_map, settled_blocks[-1])

            continue

        # compare block with height map to find its Z values
        heighest_z = 0
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if height_map[y][x] > heighest_z:
                    heighest_z = height_map[y][x]

        settled_blocks.append(
            (block_id, (x1, y1, heighest_z + 1), (x2, y2, (heighest_z + 1) + (z2 - z1)))
        )
        update_height_map(height_map, settled_blocks[-1])

    return settled_blocks


def update_height_map(height_map, block):
    _, (x1, y1, _), (x2, y2, z2) = block

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if height_map[y][x] < z2:
                height_map[y][x] = z2


def solution(input_blocks, part):
    sorted_blocks = sorted(input_blocks, key=cmp_to_key(sort_by_z))

    # add index as "id" for the blocks because the disingrate check requires
    # _something_ unique per block otherwise a block with the same x/y values
    # but different z might be flagged as safe to disingrate if it isn't.

    sorted_blocks_with_id = [
        (block_id, *block) for block_id, block in enumerate(sorted_blocks)
    ]

    settled_blocks = settle_blocks(sorted_blocks_with_id)
    settled_blocks_set = set(settled_blocks)

    collapsed_blocks = []

    for block in settled_blocks:
        disintegrated_blocks_set = set(settle_blocks(settled_blocks, block))

        collapsed_blocks.append(len(disintegrated_blocks_set - settled_blocks_set))

    match part:
        case 1:
            return len([v for v in collapsed_blocks if v == 0])
        case 2:
            return sum(collapsed_blocks)


print("—")
print(f"Solution 01: {solution(input_blocks, 1)}")
print(f"Solution 02: {solution(input_blocks, 2)}")
print("—")
