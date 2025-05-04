import re

with open("input.txt") as file:
    data = file.read()

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

mul_matches = pattern.findall(data)

result = sum([int(pair_values[0]) * int(pair_values[1]) for pair_values in mul_matches])

print(result)
