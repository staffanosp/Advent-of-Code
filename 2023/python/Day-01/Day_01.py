with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


def solution01(input_data):
    return sum(
        [
            int("".join([numbers[0], numbers[-1]]))
            for numbers in [
                [char for char in string if char.isdigit()] for string in input_data
            ]
        ]
    )


def solution02(input_data):
    substrings_and_digits = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]

    calibration_values = []

    for line in input_data:
        # first digit
        first_digit = None
        last_digit = None
        min_index = len(line)
        max_index = -1

        for substring, digit in substrings_and_digits:
            # first digit
            if min_index > 0:
                index = line.find(substring)
                if index != -1:
                    if index < min_index:
                        min_index = index
                        first_digit = digit

            # last digit
            if max_index < len(line) - 1:
                index = line.rfind(substring)
                if index != -1:
                    if index > max_index:
                        max_index = index
                        last_digit = digit

            # stop searching if digits are at the very beginning and end
            if min_index == 0 and max_index == len(line) - 1:
                break

        calibration_values.append(int(first_digit + last_digit))

    return sum(calibration_values)


print("—")
print(f"Solution 01: {solution01(input_data)}")
print(f"Solution 02: {solution02(input_data)}")
print("—")
