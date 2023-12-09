with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            times = [int(n) for n in line.strip().split()[1:]]
        if i == 1:
            distances = [int(n) for n in line.strip().split()[1:]]

races = list(zip(times, distances))


def multiply(list):
    product = 1
    for number in list:
        product *= number
    return product


def solution01(races):
    possible_wins = []

    for race_time, record_distance in races:
        curr_possible_wins = 0

        for ms in range(race_time + 1):
            speed = ms
            remaining_time = race_time - ms

            distance = speed * remaining_time

            if distance > record_distance:
                curr_possible_wins += 1

        possible_wins.append(curr_possible_wins)

    return multiply(possible_wins)


def solution02(races):
    race_time = int("".join([str(v[0]) for v in races]))
    record_distance = int("".join([str(v[1]) for v in races]))

    step_size = round(race_time / 10000)

    first_win_by_step_size_ms = None
    first_win_ms = None

    last_win_by_step_size_ms = None
    last_win_ms = None

    # 1. Find first win and last win by step_size
    for ms in range(0, race_time, step_size):
        # print(ms)
        speed = ms
        remaining_time = race_time - ms
        distance = speed * remaining_time

        if distance > record_distance and not first_win_by_step_size_ms:
            first_win_by_step_size_ms = ms

        if distance < record_distance and first_win_by_step_size_ms:
            last_win_by_step_size_ms = ms
            break

    # 2. Find the actual ms values
    # first win
    for ms in range(first_win_by_step_size_ms - step_size, race_time):
        speed = ms
        remaining_time = race_time - ms
        distance = speed * remaining_time

        if distance > record_distance:
            first_win_ms = ms
            break

    # last win
    for ms in range(last_win_by_step_size_ms - step_size, race_time):
        speed = ms
        remaining_time = race_time - ms
        distance = speed * remaining_time

        if distance < record_distance:
            last_win_ms = ms - 1  # -1 because the last win was the prev ms
            break

    return last_win_ms - first_win_ms + 1  # +1 to include the last win


print("—")
print(f"Solution 01: {solution01(races)}")
print(f"Solution 02: {solution02(races)}")
print("—")
