def find_max(numbers):
    current_max = None

    if not numbers:
        return None

    for number in numbers:
        if current_max is None or number > current_max:
            current_max = number

    return current_max


def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def count_occurrences(items, target):
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count
