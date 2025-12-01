rotations = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        rotations.append((line[0], int(line[1:])))


def solution01(rotations):
    dial = 50

    times_at_0 = 0

    for direction, steps in rotations:
        match direction:
            case "L":
                dial -= steps
            case "R":
                dial += steps

        dial %= 100

        if dial == 0:
            times_at_0 += 1

    return times_at_0


def solution02(rotations):
    dial = 50
    times_at_0 = 0

    for direction, steps in rotations:
        for _ in range(steps):
            match direction:
                case "L":
                    dial -= 1
                case "R":
                    dial += 1

            dial %= 100

            if dial == 0:
                times_at_0 += 1

    return times_at_0


print("—")
print(f"Solution 01: {solution01(rotations)}")
print(f"Solution 02: {solution02(rotations)}")
print("—")
