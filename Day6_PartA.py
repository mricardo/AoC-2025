import re

with open("Day6_Input.txt", "r") as file:
    data = file.read().strip()

problems = [re.split(r'\s+', line.strip()) for line in data.strip().splitlines()]
problems = [list(col) for col in zip(*problems)]

print(problems)

total = 0
for problem in problems:
    operator = problem[-1]
    total += eval(operator.join(problem[:-1]))

print(total)