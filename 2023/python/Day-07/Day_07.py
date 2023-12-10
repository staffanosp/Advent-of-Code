import functools

with open("input.txt", "r") as f:
    hands = {
        hand: {"bid": int(bid)}
        for hand, bid in [line.strip().split() for line in f.readlines()]
    }


def compare_hands(labels_to_strength):
    def compare_func(a, b):
        a_hand = a[0]
        a_score = a[1]["score"]
        b_hand = b[0]
        b_score = b[1]["score"]

        if a_score > b_score:
            return 1
        elif a_score < b_score:
            return -1
        else:
            for a_card, b_card in zip(a_hand, b_hand):
                a_card_score = labels_to_strength[a_card]
                b_card_score = labels_to_strength[b_card]

                if a_card_score > b_card_score:
                    return 1
                elif a_card_score < b_card_score:
                    return -1

    return compare_func


def solution(hands, part):
    hands = hands.copy()

    labels_to_strength = {
        1: {
            label: i
            for i, label in enumerate(
                ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
            )
        },
        2: {
            label: i
            for i, label in enumerate(
                ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
            )
        },
    }

    for hand in hands:
        card_counts = {}
        j_counts = 0
        for card in hand:
            if part == 2:
                if card == "J":
                    j_counts += 1
                    continue

            if card in card_counts:
                card_counts[card] += 1
            else:
                card_counts[card] = 1

        card_counts = sorted(card_counts.values())

        if part == 2:
            if j_counts == 5:  # special case for handling a hand with 5 J:s
                card_counts.append(5)
            else:
                card_counts.append(card_counts.pop() + j_counts)

        # evaluate hand
        match card_counts[::-1]:
            case [5]:
                hands[hand]["score"] = 6
            case [4, 1]:
                hands[hand]["score"] = 5
            case [3, 2]:
                hands[hand]["score"] = 4
            case [3, 1, 1]:
                hands[hand]["score"] = 3
            case [2, 2, 1]:
                hands[hand]["score"] = 2
            case [2, 1, 1, 1]:
                hands[hand]["score"] = 1
            case [1, 1, 1, 1, 1]:
                hands[hand]["score"] = 0

    sorted_hands = sorted(
        hands.items(), key=functools.cmp_to_key(compare_hands(labels_to_strength[part]))
    )

    winnings = [hand[1]["bid"] * (i + 1) for i, hand in enumerate(sorted_hands)]

    return sum(winnings)


print("—")
print(f"Solution 01: {solution(hands, 1)}")
print(f"Solution 02: {solution(hands, 2)}")
print("—")
