from time import perf_counter

seeds_line = []
conversion_steps = []

with open("input.txt", "r") as f:
    conversion_maps = []

    for i, line in enumerate((line.strip() for line in f.readlines())):
        if i == 0:
            seeds_line = [int(n) for n in line.split(": ")[1].split()]
            continue

        if line == "":
            if conversion_maps:
                conversion_steps.append(conversion_maps)
                conversion_maps = []

            continue

        if line[0].isdigit():
            conversion_maps.append([int(n) for n in line.split()])

    conversion_steps.append(conversion_maps)


def solution(seeds_line, conversion_steps, part):
    start_time = perf_counter()

    if part == 1:
        print("————— Solution 01 start —————")

        print_interval = 1
        seeds_len = len(seeds_line)
        seeds = seeds_line

    elif part == 2:
        print("————— Solution 02 start —————")

        print_interval = 1_000_000
        seeds_len = sum([range for range in seeds_line[1::2]])
        seeds = (
            seed
            for i in range(0, len(seeds_line), 2)
            for seed in range(seeds_line[i], seeds_line[i] + seeds_line[i + 1])
        )

    min_location = None
    for i, seed in enumerate(seeds):
        if i % print_interval == 0 or i == seeds_len - 1:
            elapsed_time = perf_counter() - start_time
            h = int(elapsed_time // 3600)
            m = int((elapsed_time % 3600) // 60)
            s = int(elapsed_time % 60)

            print(
                "iteration:",
                i,
                "\t",
                "min_location:",
                min_location,
                "\t",
                "seed:",
                seed,
                "\t",
                "progress:",
                "{:.2f}%".format((i / (seeds_len - 1)) * 100),
                "\t",
                "elapsed time:",
                f"{h:02}h {m:02}m {s:02}s",
            )

        for conversion_step in conversion_steps:
            for dst_range_start, src_range_start, range_len in conversion_step:
                if src_range_start <= seed < src_range_start + range_len:
                    new_seed = seed + dst_range_start - src_range_start
                else:
                    new_seed = seed

                if seed != new_seed:
                    break

            seed = new_seed

        if min_location == None or seed < min_location:
            min_location = seed

    return min_location


solution01 = solution(seeds_line, conversion_steps, 1)
solution02 = solution(seeds_line, conversion_steps, 2)


print("—")
print(f"Solution 01: {solution01}")
print(f"Solution 02: {solution02}")
print("—")
