input_section = 0  # 0: rules, 1: updates

ordering_rules = []
updates = []

with open("input.txt", "r") as f:
    for line in [line.strip() for line in f.readlines()]:

        if line == "":
            input_section += 1
            continue

        match input_section:
            case 0:  # ordering rules
                ordering_rules.append(tuple([int(v) for v in line.split("|")]))

            case 1:  # updates
                updates.append([int(v) for v in line.split(",")])


def is_valid(update, ordering_rules):
    for n_pos, n in enumerate(update):
        for a, b in ordering_rules:
            if a == n:
                if b in update[:n_pos]:
                    return False

    return True


def fix(update, ordering_rules):
    update = update[:]

    while not is_valid(update, ordering_rules):
        for n_pos, n in enumerate(update):
            for a, b in ordering_rules:
                if a == n:
                    if b in update[:n_pos]:
                        b_index = update.index(b)
                        update[n_pos], update[b_index] = update[b_index], update[n_pos]

    return update


def solution01(ordering_rules, updates):
    return sum(
        [
            update[len(update) // 2]
            for update in updates
            if is_valid(update, ordering_rules)
        ]
    )


def solution02(ordering_rules, updates):
    fixed_updates = [
        fix(update, ordering_rules)
        for update in updates
        if not is_valid(update, ordering_rules)
    ]

    return sum([update[len(update) // 2] for update in fixed_updates])


print("—")
print(f"Solution 01: {solution01(ordering_rules, updates)}")
print(f"Solution 02: {solution02(ordering_rules, updates)}")
print("—")
