from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
        
    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty stack")
        return self._items.popleft()
    
    def peek(self):
        if not self._items:
            return None
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)