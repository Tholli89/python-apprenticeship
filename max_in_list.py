numbers = [3, 7, 2, 9, 4]

#assume the first element is the current max
current_max = numbers[0]

for value in numbers:
    if value > current_max:
        current_max = value

print("The maximum value is: ", current_max)