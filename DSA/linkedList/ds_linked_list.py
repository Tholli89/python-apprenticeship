class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next

        return None
    
    def delete_first(self, value):
        if self.head is None:
            return False

        current = self.head

        if current.value == value:
            self.head = current.next
            return True

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
            
        return False
    
    def to_list(self):
        conversionList = []

        current = self.head
        
        while current is not None:
            conversionList.append(current.value)
            current = current.next

        return conversionList