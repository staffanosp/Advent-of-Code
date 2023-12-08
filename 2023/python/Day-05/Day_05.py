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


def solution01(seeds_line, conversion_steps):
    seed_conversions = [[seed] for seed in seeds_line]

    for i in range(len(seed_conversions)):
        for conversion_step in conversion_steps:
            v = seed_conversions[i][-1]

            for dst_range_start, src_range_start, range_len in conversion_step:
                if src_range_start <= v <= src_range_start + range_len:
                    new_v = v + dst_range_start - src_range_start
                else:
                    new_v = v

                if v != new_v:
                    break

            seed_conversions[i].append(new_v)

    return min([v[-1] for v in seed_conversions])


print("—")
print(f"Solution 01: {solution01(seeds_line, conversion_steps)}")
print("—")
