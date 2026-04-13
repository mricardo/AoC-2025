from itertools import zip_longest

with open("Day6_Input.txt") as file:
    lines = file.read().splitlines()

total = subtotal = 0
operator = None

for col in zip_longest(*lines, fillvalue=' '):
    col_str = ''.join(col)
    
    if col_str[-1] != ' ':
        operator = col_str[-1]
        number_str = col_str[:-1].strip()
    else:
        number_str = col_str.strip()
    
    if not number_str:
        total += subtotal
        subtotal = 0
        continue 

    value = int(number_str)

    if operator == '+':
        subtotal += value
    elif operator == '*':
        subtotal = (subtotal or 1) * value 

total += subtotal
print(total)