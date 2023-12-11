import copy
from collections import deque


with open("input.txt", "r") as f:
    input_data = [[int(n) for n in line.strip().split()] for line in f.readlines()]


def solution01(input_data):
    histories = copy.deepcopy(input_data)

    for hist_i in range(len(histories)):
        sequences = [histories[hist_i]]

        # "go down" to only 0s
        while any(n != 0 for n in sequences[-1]):
            sequences.append(
                [
                    sequences[-1][i + 1] - sequences[-1][i]
                    for i in range(len(sequences[-1]) - 1)
                ]
            )

        # extrapolate forward
        sequences = sequences[::-1]
        for seq_i in range(len(sequences)):
            if seq_i == 0:
                sequences[seq_i].append(0)
                continue

            sequences[seq_i].append(sequences[seq_i][-1] + sequences[seq_i - 1][-1])

        histories[hist_i].append(sequences[-1][-1])

    return sum([n[-1] for n in histories])


def solution02(input_data):
    histories = [deque(history) for history in input_data]

    for hist_i in range(len(histories)):
        sequences = [histories[hist_i]]

        # "go down" to only 0s
        while any(n != 0 for n in sequences[-1]):
            sequences.append(
                [
                    sequences[-1][i + 1] - sequences[-1][i]
                    for i in range(len(sequences[-1]) - 1)
                ]
            )

        # extrapolate backward
        sequences = [deque(sequence) for sequence in sequences[::-1]]
        for seq_i in range(len(sequences)):
            if seq_i == 0:
                sequences[seq_i].appendleft(0)
                continue

            sequences[seq_i].appendleft(sequences[seq_i][0] - sequences[seq_i - 1][0])

        histories[hist_i].appendleft(sequences[-1][0])

    return sum([n[0] for n in histories])


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
