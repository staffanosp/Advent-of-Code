ranges = []
ingredients = []

part = 0

with open("input.txt", "r") as f:

    for line in [line.strip() for line in f.readlines()]:
        if not line:
            part += 1
            continue

        match part:
            case 0:  # range
                a, b = line.split("-")

                ranges.append((int(a), int(b)))

                pass
            case 1:  # ingredient
                ingredients.append(int(line))
                pass


def isFresh(ingredient, ranges):
    for a, b in ranges:
        if a <= ingredient <= b:
            return True
    return False


def solution01(ranges, ingredients):

    fresh_ingredients = 0

    for ingredient in ingredients:

        if isFresh(ingredient, ranges):
            fresh_ingredients += 1

    return fresh_ingredients


def solution02(ranges):

    compressed_ranges = []

    for new_a, new_b in sorted(ranges):

        was_handled = False
        for j, (comp_a, comp_b) in enumerate(sorted(compressed_ranges)):

            new_a_in_range = comp_a <= new_a <= comp_b
            new_b_in_range = comp_a <= new_b <= comp_b

            if new_a_in_range and new_b_in_range:
                was_handled = True
                break

            if new_a_in_range:
                compressed_ranges[j][1] = new_b
                was_handled = True
                break

        if not was_handled:
            compressed_ranges.append([new_a, new_b])

    return sum([b - a + 1 for a, b in compressed_ranges])


print("—")
print(f"Solution 01: {solution01(ranges, ingredients)}")
print(f"Solution 02: {solution02(ranges)}")
print("—")
