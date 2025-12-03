with open("Day1/Day1_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

dial = 50
password = 0

for line in lines: 
    rotations = int(line[1:])
    password += (rotations // 100) if rotations >= 100 else 0
    rotations = rotations % 100

    if line[0] == "L":
        new_dial = (dial - rotations) % 100
    elif line[0] == "R":
        new_dial = (dial + rotations) % 100

    if new_dial == 0:
        password += 1
    elif dial != 0 and new_dial < dial and line[0] == "R":
        password += 1
    elif dial != 0 and new_dial > dial and line[0] == "L":
        password += 1
    
    dial = new_dial

print(password)
