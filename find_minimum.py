numbers = [34, 432, 1, 99]

# 最小値
minimum_number = numbers[0]

for number in numbers:
    if minimum_number > number:
        minimum_number = number
print(minimum_number)