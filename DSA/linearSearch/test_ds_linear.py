import pytest
from ds_linear import find_max, linear_search, count_occurrences

def test_find_max_normal():
    numbers = [3, 1, 7, 4]
    assert find_max(numbers) == 7

def test_find_max_all_negative():
    numbers = [-5, -2, -9]
    assert find_max(numbers) == -2

def test_find_max_empty():
    numbers = []
    assert find_max(numbers) == None

def test_linear_search_found():
    numbers = [3, 1, 7, 4]
    target = 7
    assert linear_search(numbers, target) == 2

def test_linear_search_not_found():
    numbers = [3, 1, 7, 4]
    target = 9
    assert linear_search(numbers, target) == -1

def test_linear_search_empty():
    numbers = []
    target = 8
    assert linear_search(numbers, target) == -1

def test_count_occurrences_some():
    numbers = [1, 2, 2, 2, 3]
    target = 2
    assert count_occurrences(numbers, target) == 3

def test_count_occurrences_zero():
    numbers = [1, 2, 2, 2, 3]
    target = 7
    assert count_occurrences(numbers, target) == 0

def test_count_occurrences_empty():
    numbers = []
    target = 7
    assert count_occurrences(numbers, target) == 0