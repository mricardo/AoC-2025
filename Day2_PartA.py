def calculated_invalid_ids(start, end):
    invalid_ids = 0
    for i in range(start, end + 1):
        str_i = str(i)
        if len(str_i) % 2 == 0:
            middle = int(len(str_i) / 2)
            first_part = str_i[0 : middle]
            second_part = str_i[middle : ]
            if first_part == second_part:
                invalid_ids += i
    return invalid_ids


with open("Day2_Input.txt") as file:
    ranges = file.read().strip().split(",")

total_sum = 0
for r in ranges:
    start_range = int(r.split("-")[0])
    end_range = int(r.split("-")[1])
    total_sum += calculated_invalid_ids(start_range, end_range)

print(f"Total Invalid Ids: {total_sum}")