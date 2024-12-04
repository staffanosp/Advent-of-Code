from collections import Counter

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


def solution01(input_data):
    h = len(input_data)
    w = len(input_data[0])

    directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    word = "XMAS"

    found_words_counter = 0

    for y in range(h):
        for x in range(w):
            if input_data[y][x] == word[0]:

                for dx, dy in directions:

                    found_word = True

                    for char_i in (i + 1 for i in range(len(word) - 1)):

                        x2 = x + dx * char_i
                        y2 = y + dy * char_i

                        if not x2 in range(w):
                            found_word = False
                            break

                        if not y2 in range(h):
                            found_word = False
                            break

                        if not input_data[y2][x2] == word[char_i]:
                            found_word = False
                            break

                    if found_word:
                        found_words_counter += 1

    return found_words_counter


def solution02(input_data):
    h = len(input_data)
    w = len(input_data[0])

    directions = [
        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1),
    ]

    crossing_coords = []
    word = "MAS"

    for y in range(h):
        for x in range(w):
            if input_data[y][x] == word[0]:

                for dx, dy in directions:

                    found_word = True

                    for char_i in (i + 1 for i in range(len(word) - 1)):

                        x2 = x + dx * char_i
                        y2 = y + dy * char_i

                        if not x2 in range(w):
                            found_word = False
                            break

                        if not y2 in range(h):
                            found_word = False
                            break

                        if not input_data[y2][x2] == word[char_i]:
                            found_word = False
                            break

                    if found_word:
                        crossing_coords.append((x + dx, y + dy))

        crossing_coords_counter = Counter(crossing_coords)

    return sum(1 for count in crossing_coords_counter.values() if count > 1)


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
