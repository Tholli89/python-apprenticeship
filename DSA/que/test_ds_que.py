import pytest
from ds_que import Queue

def test_enqueue_and_dequeue_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

def test_peek_does_not_remove():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1
    assert queue.__len__() == 3

def test_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    assert queue.is_empty() ==False

def test_dequeue_empty_raises():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

