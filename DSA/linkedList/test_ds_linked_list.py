import pytest
from ds_linked_list import SinglyLinkedList

def test_insert_at_head_orders_correctly():
    lst = SinglyLinkedList()

    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)

    assert lst.to_list() == [1, 2, 3]

def test_append_orders_correctly():
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert lst.to_list() == [1, 2, 3]

def test_find_existing_and_missing():
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert lst.find(3) == lst.head.next.next
    assert lst.find(5) == None

def test_delete_head():
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert lst.delete_first(1) == True
    assert lst.to_list() == [2, 3]

def test_delete_middle():
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert lst.delete_first(2) == True
    assert lst.to_list() == [1, 3]

def test_delete_missing():
    lst = SinglyLinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert lst.delete_first(5) == False
    assert lst.to_list() == [1, 2, 3]