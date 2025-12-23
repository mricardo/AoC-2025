with open("Day3_Input.txt") as f:
    banks = [list(b.strip()) for b in f.read().split()]

def max_number(bank, current_number, current_idx, current_length, max_length):
    if current_length >= max_length:
        return current_number

    current_max_number = -1
    for i in range(current_idx, len(bank)):
        if ((len(bank) - i) < (max_length - current_length)):
            break

        digit = bank[i]
        candidate_number = int(''.join(current_number + [digit]))
      
        if candidate_number > current_max_number:
            current_max_number = candidate_number
            current_idx = i

    if current_max_number == -1:
        return current_number

    current_number = list(str(current_max_number))

    return max_number(bank, current_number, current_idx + 1, current_length + 1, max_length)

total_jolts = 0
for bank in banks:
    total_jolts += int(''.join(max_number(bank, [], 0, 0, 12)))

print("Total jolts: ", total_jolts)