with open("Day1/Day1_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

dial = 50
password = 0
for line in lines:
    if line[0] == "L":
        dial =  (dial - int(line[1:])) % 100
    elif line[0] == "R":
        dial = (dial + int(line[1:])) % 100

    if dial == 0:
        password += 1

print(password)
