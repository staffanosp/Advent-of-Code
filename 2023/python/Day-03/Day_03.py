with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


def is_symbol(char):
    return not char in "0123456789."


def get_adj_coords(start_x, end_x, y):
    adj_coords = []

    for adj_y in range(y - 1, y + 2):
        if adj_y == y:
            adj_coords.append((start_x - 1, y))
            adj_coords.append((end_x + 1, y))

        else:
            for adj_x in range(start_x - 1, end_x + 2):
                adj_coords.append((adj_x, adj_y))

    return adj_coords


def solution(input_data, part):
    symbols = []
    gears = []
    numbers = []

    # store numbers, symbols and gears
    for y, line in enumerate(input_data):
        number_start_x = None
        curr_number = ""

        for x, char in enumerate(line):
            if char.isdigit():
                if not curr_number:
                    number_start_x = x

                curr_number += char

                # store number at end of lines
                if x == len(line) - 1:
                    numbers.append((int(curr_number), number_start_x, x, y))

            else:
                # store number
                if curr_number:
                    numbers.append((int(curr_number), number_start_x, x - 1, y))
                    number_start_x = None
                    curr_number = ""

                # store symbols
                if is_symbol(char):
                    symbols.append((x, y))

                    # store gears
                    if char == "*":
                        gears.append((x, y))

    if part == 1:
        return sum(
            [
                number
                for number, start_x, end_x, y in numbers
                if set(get_adj_coords(start_x, end_x, y)) & set(symbols)
            ]
        )

    elif part == 2:
        gear_ratios = []

        for gear in gears:
            adj_numbers = []

            for number, start_x, end_x, y in numbers:
                if gear in get_adj_coords(start_x, end_x, y):
                    adj_numbers.append(number)

            if len(adj_numbers) == 2:
                gear_ratios.append(adj_numbers[0] * adj_numbers[1])

        return sum(gear_ratios)


print("—")
print(f"Solution 01: {solution(input_data,1)}")
print(f"Solution 02: {solution(input_data,2)}")

print("—")
