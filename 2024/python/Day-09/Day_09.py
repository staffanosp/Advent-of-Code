from collections import deque

with open("input.txt", "r") as f:
    input_data = f.read().strip()


FREE_SPACE = "."


def get_checksum(blocks):
    pos_counter = 0
    checksum = 0
    for block_size, block_id in blocks:
        if block_id == FREE_SPACE:
            pos_counter += block_size
            continue

        for _ in range(block_size):
            checksum += int(block_id) * pos_counter
            pos_counter += 1

    return checksum


def convert_to_blocks(data):
    # [(block_size, id),...]
    blocks = deque()
    for i, block in enumerate(input_data):
        is_free_space = i % 2 != 0

        block_size = int(block)
        block_id = str(i // 2) if not is_free_space else FREE_SPACE

        blocks.append((block_size, block_id))

    return blocks


def solution01(input_data):

    blocks = convert_to_blocks(input_data)

    compressed_blocks = []
    while blocks:

        block_size, block_id = blocks.popleft()

        if block_id == FREE_SPACE:
            free_size = block_size

            while free_size > 0 and blocks:
                block2_size, block2_id = blocks.pop()

                if block2_id == FREE_SPACE:
                    continue

                if block2_size <= free_size:
                    compressed_blocks.append((block2_size, block2_id))
                    free_size -= block2_size

                else:
                    compressed_blocks.append((free_size, block2_id))
                    blocks.append((block2_size - free_size, block2_id))

                    free_size = 0
            continue

        compressed_blocks.append((block_size, block_id))

    return get_checksum(compressed_blocks)


def solution02(input_data):

    blocks = convert_to_blocks(input_data)

    compressed_blocks = []

    while blocks:

        block_size, block_id = blocks.popleft()

        if block_id == FREE_SPACE:

            tail = deque()
            free_size = block_size

            moved = False

            while not moved and blocks:
                block2_size, block2_id = blocks.pop()

                if not block2_id == FREE_SPACE and block2_size <= free_size:
                    compressed_blocks.append((block2_size, block2_id))
                    tail.appendleft((block2_size, FREE_SPACE))
                    free_size -= block2_size

                    if free_size > 0:
                        blocks.appendleft((free_size, FREE_SPACE))

                    moved = True

                else:
                    tail.appendleft((block2_size, block2_id))

            if not moved:
                compressed_blocks.append((block_size, block_id))

            blocks.extend(tail)

        else:

            compressed_blocks.append((block_size, block_id))

    return get_checksum(compressed_blocks)


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
