from collections import defaultdict

with open("input.txt", "r") as f:
    input_data = [int(v) for v in f.read().strip().split()]


def solution(input_data, steps):
    stones = defaultdict(int)

    for stone in input_data:
        stones[stone] += 1

    for _ in range(steps):
        new_stones = defaultdict(int)

        for stone, stone_n in stones.items():

            new_stones[stone] += -stone_n

            # rule 1
            if stone == 0:
                new_stones[1] += stone_n
                continue

            # rule 2
            stone_string = str(stone)
            stone_digit_len = len(stone_string)
            if stone_digit_len % 2 == 0:
                new_stones[int(stone_string[: stone_digit_len // 2])] += stone_n
                new_stones[int(stone_string[stone_digit_len // 2 :])] += stone_n
                continue

            # rule 3
            new_stones[stone * 2024] += stone_n

        for k, v in new_stones.items():
            stones[k] += v

    return sum(stones.values())


print("—")
print(f"Solution 01: {solution(input_data,25)}")
print(f"Solution 02: {solution(input_data,75)}")
print("—")
