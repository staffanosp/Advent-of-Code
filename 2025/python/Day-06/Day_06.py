import math


def try_int(n):
    try:
        return int(n)
    except:
        return n


op = {
    "+": sum,
    "*": math.prod,
}


# parse part 1
with open("input.txt", "r") as f:
    problems_part1 = list(
        zip(*[[try_int(x) for x in line.strip().split()] for line in f.readlines()])
    )

# parse part 2
with open("input.txt", "r") as f:
    problems_part2 = []

    raw_data = [line.replace("\n", "") for line in f.readlines()]

    w = max(len(line) for line in raw_data)
    h = len(raw_data)

    curr_problem = []
    curr_operator = ""
    for x in range(w):
        num = []

        for y in range(h):

            char = raw_data[y][x].strip()  # strip to ignore " "

            if char:
                if y == h - 1:  # last line is the operator
                    curr_operator = char
                    break

                num.append(char)

        if num:
            curr_problem.append(int("".join(num)))

        # new or last problem
        if not num or x == w - 1:

            problems_part2.append(tuple([*curr_problem, curr_operator]))

            curr_problem = []
            curr_operator = ""


def solution(problems):
    return sum([op[x[-1]](x[:-1]) for x in problems])


print("—")
print(f"Solution 01: {solution(problems_part1)}")
print(f"Solution 02: {solution(problems_part2)}")
print("—")
