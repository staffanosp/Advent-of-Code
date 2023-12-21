from collections import deque

workflows = {}
parts = []

target = "workflows"

with open("input.txt", "r") as f:
    for line in [line.strip() for line in f.readlines()]:
        if line == "":
            target = "parts"
            continue

        match target:
            case "workflows":
                name, rules_raw = line[:-1].split("{")

                rules = []

                for rule in rules_raw.split(","):
                    cat = None
                    op = None
                    v = None
                    dest = None

                    rule = rule.split(":")

                    if len(rule) > 1:
                        cat = rule[0][0]
                        op = rule[0][1]
                        v = int(rule[0][2:])
                        dest = rule[1]
                    else:
                        dest = rule[0]

                    rules.append((cat, op, v, dest))

                workflows[name] = rules

            case "parts":
                part = {}
                for cat, rating in [part.split("=") for part in line[1:-1].split(",")]:
                    part[cat] = int(rating)

                parts.append(part)


def test(a, b, op):
    if op == ">":
        return a > b
    if op == "<":
        return a < b


def multiply(list):
    product = 1
    for number in list:
        product *= number
    return product


def solution01(parts, workflows):
    accepted = []
    rejected = []

    start_workflow = "in"

    parts_queue = deque([(start_workflow, part) for part in parts])

    while parts_queue:
        workflow, part = parts_queue.popleft()

        for cat, op, v, dest in workflows[workflow]:
            if op:
                if not test(part[cat], v, op):
                    continue

            match dest:
                case "A":
                    accepted.append(part)

                case "R":
                    rejected.append(part)

                case _:
                    parts_queue.append((dest, part))

            break

    return sum(sum(part.values()) for part in accepted)


def solution02(workflows):
    def send_to_destination(combination, dest):
        match dest:
            case "A":
                accepted.append(combination)

            case "R":
                rejected.append(combination)

            case _:
                combinations_queue.append((dest, combination))

    accepted = []
    rejected = []

    start_workflow = "in"

    combinations_queue = deque(
        [
            (
                start_workflow,
                {
                    "x": (1, 4000),
                    "m": (1, 4000),
                    "a": (1, 4000),
                    "s": (1, 4000),
                },
            )
        ]
    )

    while combinations_queue:
        workflow, curr_combination = combinations_queue.popleft()
        for cat, op, v, dest in workflows[workflow]:
            if op:
                min_range, max_range = curr_combination[cat]

                # Split the range
                lo_min_range = min_range
                lo_max_range = v if op == ">" else v - 1
                hi_min_range = v if op == "<" else v + 1
                hi_max_range = max_range

                lo_combination = curr_combination.copy()
                lo_combination[cat] = (lo_min_range, lo_max_range)

                hi_combination = curr_combination.copy()
                hi_combination[cat] = (hi_min_range, hi_max_range)

                # Which part should be kept in current workflow
                # and which part is the "new" part?
                if test(lo_min_range, v, op) and test(lo_max_range, v, op):
                    new_combination = lo_combination
                    curr_combination = hi_combination
                else:
                    new_combination = hi_combination
                    curr_combination = lo_combination

                # Send new combination to its destination.
                # The current combination will continue in the current workflow
                send_to_destination(new_combination, dest)

            else:
                send_to_destination(curr_combination, dest)
                break

    return sum(
        [
            multiply(diff)
            for diff in [
                [rng[1] - rng[0] + 1 for rng in ranges.values()] for ranges in accepted
            ]
        ]
    )


print("—")
print(f"Solution 01: {solution01(parts,workflows)}")
print(f"Solution 02: {solution02(workflows)}")
print("—")
