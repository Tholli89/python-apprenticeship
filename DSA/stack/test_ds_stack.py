import pytest
from ds_stack import Stack

def test_push_and_pop_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_peek_does_not_remove():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.__len__() == 3

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() ==False

def test_pop_empty_raises():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

