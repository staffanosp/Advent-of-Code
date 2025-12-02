with open("input.txt", "r") as f:
    input_data = [
        (
            int(v[0]),
            int(v[1]),
        )
        for v in [range.split("-") for range in f.read().strip().split(",")]
    ]


def validate_part1(v):
    v = str(v)

    a = v[: len(v) // 2]
    b = v[len(v) // 2 :]

    if a == b:
        return False

    return True


def validate_part2(id_):
    id_ = str(id_)

    max_chunk_l = len(id_) // 2

    for chunk_size in range(1, max_chunk_l + 1):

        if len(id_) % chunk_size != 0:
            continue

        chunks = set((id_[x : x + chunk_size] for x in range(0, len(id_), chunk_size)))

        if len(chunks) == 1:
            return False

    return True


def solution(input_data, part):

    validation_func = {
        1: validate_part1,
        2: validate_part2,
    }

    acc = 0

    for start, end in input_data:
        for id_ in range(start, end + 1):
            if not validation_func[part](id_):
                acc += id_

    return acc


print("—")
print(f"Solution 01: {solution(input_data,1)}")
print(f"Solution 02: {solution(input_data,2)}")
print("—")
