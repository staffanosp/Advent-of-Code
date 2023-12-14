from itertools import product

with open("input.txt", "r") as f:
    input_data = [
        (conditions, tuple([int(n) for n in groups.split(",")]))
        for conditions, groups in [line.strip().split() for line in f.readlines()]
    ]


def to_groups(conditions):
    return tuple([len(group) for group in conditions.split(".") if group != ""])


def solution01(input_data):
    possible_arrangements_sums = []

    for conditions, groups in input_data:
        possible_arrangements_sum = 0

        unknowns_n = len([c for c in conditions if c == "?"])
        possible_states = [list(x) for x in product([".", "#"], repeat=unknowns_n)]

        for state in possible_states:
            arrangement_to_test = ""

            for c in conditions:
                arrangement_to_test += state.pop() if c == "?" else c

            if to_groups(arrangement_to_test) == groups:
                possible_arrangements_sum += 1

        possible_arrangements_sums.append(possible_arrangements_sum)

    return sum(possible_arrangements_sums)


print("—")
print(f"Solution 01: {solution01(input_data)}")
print("—")
