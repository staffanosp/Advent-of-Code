numbers_a = []
numbers_b = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        a, b = line.strip().split()
        numbers_a.append(int(a))
        numbers_b.append(int(b))


def solution01(numbers_a, numbers_b):
    return sum([abs(a - b) for a, b in zip(sorted(numbers_a), sorted(numbers_b))])


def solution02(numbers_a, numbers_b):
    return sum([a * numbers_b.count(a) for a in numbers_a])


print("—")
print(f"Solution 01: {solution01(numbers_a, numbers_b)}")
print(f"Solution 02: {solution02(numbers_a, numbers_b)}")
print("—")
