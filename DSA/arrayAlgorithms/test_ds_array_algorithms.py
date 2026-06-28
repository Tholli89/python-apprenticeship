import pytest
from ds_array_algorithms import reverse_in_place, second_largest, move_zeroes_to_end

def test_reverse_in_place_even_length():
    items = ["apple", "banana", "strawberry", "grape"]
    reverse_in_place(items)
    assert len(items) == 4

def test_reverse_in_place_odd_length():
    items = ["apple", "banana", "strawberry", "grape", "kiwi"]
    reverse_in_place(items)
    assert len(items) == 5

def test_reverse_in_place_empty():
    items = []
    reverse_in_place(items)
    assert len(items) == 0

def test_second_largest_normal():
    numbers = [1, 5, 3, 4]
    assert second_largest(numbers) == 4

def test_second_largest_with_duplicates():
    numbers = [5, 5, 4, 4, 3]
    assert second_largest(numbers) == 4

def test_second_largest_not_enough_values():
    numbers = []
    assert second_largest(numbers) == None

    numbers = [7]
    assert second_largest(numbers) == None

    numbers = [5, 5, 5]
    assert second_largest(numbers) == None

def test_move_zeroes_mixed():
    numbers = [0, 1, 0, 3, 12]
    move_zeroes_to_end(numbers) 
    assert numbers == [1, 3, 12, 0, 0]

def test_move_zeroes_all_zero():
    numbers = [0, 0, 0, 0, 0]
    move_zeroes_to_end(numbers) 
    assert numbers == [0, 0, 0, 0, 0]

def test_move_zeroes_no_zero():
    numbers = [5, 6, 7, 9, 4]
    move_zeroes_to_end(numbers) 
    assert numbers == [5, 6, 7, 9, 4]

def test_move_zeroes_empty():
    numbers = []
    move_zeroes_to_end(numbers)
    assert numbers == []