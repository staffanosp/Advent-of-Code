from itertools import product

input_data = []

with open("input.txt", "r") as f:
    for line in [line.strip() for line in f.readlines()]:
        test_v, numbers = line.split(": ")

        test_v = int(test_v)
        numbers = [int(n) for n in numbers.split(" ")]

        input_data.append([test_v, numbers])


def solution(input_data, part=1):
    all_ops = [
        "+",
        "*",
    ]
    if part == 2:
        all_ops.append("||")

    solved_values = []
    for test_v, numbers in input_data:

        possible_ops_combinations = list(product(all_ops, repeat=len(numbers) - 1))

        solved = False

        for ops in possible_ops_combinations:
            v = numbers[0]
            for i in range(len(numbers) - 1):
                op = ops[i]
                n = numbers[i + 1]

                match op:
                    case "+":
                        v = v + n
                    case "*":
                        v = v * n
                    case "||":
                        v = int(str(v) + str(n))

            if v == test_v:
                solved = True
                break

        if solved:
            solved_values.append(test_v)
            continue

    return sum(solved_values)


print("—")
print(f"Solution 01: {solution(input_data)}")
print(f"Solution 02: {solution(input_data,2)}")
print("—")
