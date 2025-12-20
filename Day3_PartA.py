with open("Day3_Input.txt") as f:
    banks = [list(b.strip()) for b in f.read().split()]

def next_value(l):
    for i in l:
        yield i

total_jolts = 0
for b in banks:
        max_jolt = -1
        
        for idx, v in enumerate(b): 
            first_digit = b[idx]            
            remaining_items = next_value(b[idx + 1:])

            for second_digit in remaining_items:
                current_jolt = int(first_digit + second_digit)
                if current_jolt > max_jolt:
                    max_jolt = current_jolt

        total_jolts += max_jolt

print("Total jolts: ", total_jolts)