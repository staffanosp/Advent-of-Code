import math
from collections import deque

with open("input.txt", "r") as f:
    input_data = [
        tuple([int(v) for v in line.strip().split(",")]) for line in f.readlines()
    ]


def get_circuits_and_distances(junction_boxes):
    circuits = deque([set([box]) for box in junction_boxes])

    distances = set()
    for a in junction_boxes:
        for b in junction_boxes:
            if a == b:
                continue

            dist = math.dist(a, b)

            if (dist, b, a) in distances:
                continue

            distances.add((dist, a, b))

    distances = list(sorted(distances))

    return circuits, distances


def solution(junction_boxes, part):

    circuits, distances = get_circuits_and_distances(junction_boxes)

    def should_continue(part):
        match part:
            case 1:
                nonlocal step
                return step < 1000

            case 2:
                nonlocal circuits
                return len(circuits) > 1

    step = 0
    while should_continue(part):

        _, a, b = distances[step]

        circuits_to_connect = []
        for _ in range(len(circuits)):

            circuit = circuits[-1]

            if (a in circuit or b in circuit) and not (a in circuit and b in circuit):
                circuits_to_connect.append(circuits.pop())

            circuits.rotate(1)

        if circuits_to_connect:
            circuits.append(set().union(*circuits_to_connect))

        step += 1

    match part:
        case 1:
            return math.prod(sorted([len(circuit) for circuit in circuits])[-3:])

        case 2:
            return a[0] * b[0]


print("—")
print(f"Solution 01: {solution(input_data,1)}")
print(f"Solution 01: {solution(input_data,2)}")
print("—")
