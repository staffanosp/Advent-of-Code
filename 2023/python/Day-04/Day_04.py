with open("input.txt", "r") as f:
    input_data = [
        [set([int(v) for v in numbers.split()]) for numbers in numbers]
        for numbers in [
            line.strip().split(": ")[1].split(" | ") for line in f.readlines()
        ]
    ]


def clamp_below_one(n):
    if n < 1:
        return 0
    return n


def solution01(cards):
    return sum(
        [
            clamp_below_one(2 ** (len(winning_numbers & my_numbers) - 1))
            for winning_numbers, my_numbers in cards
        ]
    )


def solution02(cards):
    cards_matching_numbers_n = [
        len(winning_numbers & my_numbers) for winning_numbers, my_numbers in cards
    ]

    cards_to_process = [i for i, _ in enumerate(cards)]

    processed_cards_counter = 0

    while cards_to_process:
        card = cards_to_process.pop()

        cards_to_process += [
            i for i in range(card + 1, card + 1 + cards_matching_numbers_n[card])
        ]

        processed_cards_counter += 1

    return processed_cards_counter


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
