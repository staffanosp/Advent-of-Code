with open("input.txt", "r") as f:
    input_data = [[int(v) for v in line.strip()] for line in f.readlines()]


def solution(battery_banks, req_length):

    acc = 0

    for bank in battery_banks:
        bank = bank[:]

        batteries = []

        for battery in range(req_length):

            batteries.append(max(bank[: len(bank) - req_length + 1 + battery]))

            last_battery_i = bank.index(batteries[-1])

            bank = bank[last_battery_i + 1 :]

        acc += int("".join([str(n) for n in batteries]))

    return acc


print("—")
print(f"Solution 01: {solution(input_data, 2)}")
print(f"Solution 02: {solution(input_data, 12)}")
print("—")
