numbers = [34, 432, 1, 99]

# 合計値
total = 0

for number in numbers:
    total += number
print(total)

# 最大値
max_number = 0

for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)

# 最小値
minimum_number = 999

for number in numbers:
    if minimum_number > number:
        minimum_number = number
print(minimum_number)