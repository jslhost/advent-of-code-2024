with open("input.txt") as file:
    data = file.read().splitlines()

# Part 1

safe_count = 0

for report in data:
    report = report.split()
    report = [int(level) for level in report]
    diff_list = []
    for i, level in enumerate(report):

        if i + 1 != len(report):
            diff = level - report[i + 1]
            diff_list.append(diff)

    if all(x > 0 for x in diff_list):  # Decreasing
        if all((x >= 1) and (x <= 3) for x in diff_list):  # Safe
            safe_count += 1

    if all(x < 0 for x in diff_list):  # Increasing
        if all((x <= -1) and (x >= -3) for x in diff_list):  # Safe
            safe_count += 1

print(safe_count)
