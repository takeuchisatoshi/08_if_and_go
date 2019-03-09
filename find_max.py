numbers = [34, 432, 1, 99]

# 最大値
max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)
