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

    return sum(
        [
            1
            for distance in (ms * (race_time - ms) for ms in range(race_time))
            if distance > record_distance
        ]
    )


print("—")
print(f"Solution 01: {solution01(races)}")
print(f"Solution 02: {solution02(races)}")
print("—")
