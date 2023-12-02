with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


input_data = [
    [
        [
            (n_color[1], int(n_color[0]))
            for n_color in [n_color.split(" ") for n_color in subset.split(", ")]
        ]
        for subset in line.split(": ")[1].split("; ")
    ]
    for line in input_data
]


def multiply(list):
    product = 1
    for number in list:
        product *= number
    return product


def solution01(input_data):
    max_colors = {"red": 12, "green": 13, "blue": 14}

    possible_game_ids = []

    for id, game in enumerate(input_data):
        id += 1  # game ids start at 1

        is_possible = True

        for subset in game:
            for color, n in subset:
                if n > max_colors[color]:
                    is_possible = False
                    break

            if not is_possible:
                break

        if not is_possible:
            continue

        possible_game_ids.append(id)

    return sum(possible_game_ids)


def solution02(input_data):
    game_powers = []

    for game in input_data:
        min_required = {"red": 0, "green": 0, "blue": 0}

        for subset in game:
            for color, n in subset:
                min_required[color] = max(min_required[color], n)

        game_powers.append(multiply(min_required.values()))

    return sum(game_powers)


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
