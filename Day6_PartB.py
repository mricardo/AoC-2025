
import re
from itertools import zip_longest
with open("Day6_Input.txt", "r") as file:
    data = file.read().strip()

problems = [list(line) for line in data.strip().splitlines()]
problems = [list(col) for col in zip_longest(*problems, fillvalue=' ')]

total = subtotal = 0

for problem in problems:
    number = None
    if problem[-1] != ' ':
        operator = problem[-1]
        number = ''.join(problem[:-1]).strip()
    else:
        number = ''.join(problem).strip()
    
    if len(number) == 0:
        total += subtotal
        subtotal = 0
        continue 

    if operator == '+':
        subtotal += int(number)
    elif operator == '*':
        if subtotal == 0:
            subtotal = 1
        subtotal *= int(number) 

#11643736116335
total += subtotal
print(total)
