with open("input.txt", "r") as f:
    reports = [
        [int(levels) for levels in report.strip().split()] for report in f.readlines()
    ]


def is_safe(report):
    direction = sign(report[0] - report[1])

    for curr, nxt in zip(report, report[1:]):
        diff = curr - nxt

        if not 1 <= diff * direction <= 3:
            return False

    return True


def sign(x):
    return (x > 0) - (x < 0)


def solution01(reports):
    return sum(1 for report in reports if is_safe(report))


def solution02(reports):
    safe_reports = []
    unsafe_reports = []

    for report in reports:
        if is_safe(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    for report in unsafe_reports:
        problem_dampened_reports = [
            report[:i] + report[i + 1 :] for i in range(len(report))
        ]

        for report in problem_dampened_reports:
            if is_safe(report):
                safe_reports.append(report)
                break

    return len(safe_reports)


print("—")
print(f"Solution 01: {solution01(reports)}")
print(f"Solution 02: {solution02(reports)}")
print("—")
