from collections import deque


init_sequence = []
with open("input.txt", "r") as f:
    for item in f.readlines()[0].strip().split(","):
        label = ""
        operation = None
        focal_length = ""

        for c in item:
            if c.isalpha():
                label += c
                continue

            if c in ["=", "-"]:
                operation = c
                continue

            if c.isdigit():
                focal_length += c
                continue

        init_sequence.append(
            (label, operation, int(focal_length) if focal_length != "" else None)
        )


def hash_func(string):
    v = 0
    for c in string:
        v += ord(c)
        v *= 17
        v %= 256
    return v


def solution01(init_sequence):
    return sum(
        [
            hash_func(
                label + operation + (str(focal_length) if focal_length != None else "")
            )
            for label, operation, focal_length in init_sequence
        ]
    )


def solution02(init_sequence):
    boxes = [deque() for _ in range(256)]

    for label, operation, focal_length in init_sequence:
        box = boxes[hash_func(label)]

        labels_in_box = [item[0] for item in box]

        match operation:
            case "-":
                if label in labels_in_box:
                    label_index = labels_in_box.index(label)

                    del box[label_index]

            case "=":
                if label in labels_in_box:
                    label_index = labels_in_box.index(label)

                    del box[label_index]

                    box.rotate(-label_index)
                    box.appendleft((label, focal_length))
                    box.rotate(label_index)
                else:
                    box.append((label, focal_length))

    focusing_power = 0

    for box_i, box in enumerate(boxes):
        for slot_i, (_, focal_length) in enumerate(box):
            focusing_power += (box_i + 1) * (slot_i + 1) * focal_length

    return focusing_power


print("—")
print(f"Solution 01: {solution01(init_sequence)}")
print(f"Solution 02: {solution02(init_sequence)}")
print("—")
