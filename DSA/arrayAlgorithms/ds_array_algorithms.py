items = ["apple", "banana", "strawberry", "grape"]
numbers = [3 , 0, 2, 1, 0, 5, 10, 7, 0, 4, 11, 8, 0, 6, 11]

def reverse_in_place(items):
    left = 0
    right = len(items) - 1

    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

    return None

def second_largest(numbers):
    largest = None
    second_largest = None

    if not numbers or len(numbers) < 2:
        return None
    
    for number in numbers:
        if largest == None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest == None or number > second_largest):
            second_largest = number

    return second_largest
        

def move_zeroes_to_end(numbers):
    if not numbers:
        return None
    
    write = 0
    for read in range(len(numbers)):
        if numbers[read] != 0:
            numbers[write], numbers[read] = numbers[read], numbers[write]
            write += 1
    return None

def main():
    reverse_in_place(items)
    second_largest(numbers)
    move_zeroes_to_end(numbers)

if __name__ == "__main__":
    main()