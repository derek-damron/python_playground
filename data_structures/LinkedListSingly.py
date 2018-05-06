import pdb

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        return
        
    def set_value(self, value):
        self.value = value
        return
        
    def set_next(self, next):
        self.next = next
        return
        
class LinkedListSingly:
    def __init__(self, head=None):
        self.head = head
        return
        
    def get_tail(self):
        if self.head is None:
            return self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current
            
    def get_length(self):
        current = self.head
        i = 0
        while current is not None:
            i += 1
            current = current.next
        return i
        
    def as_list(self):
        l = []
        if self.head is not None:
            current = self.head
            while current is not None:
                l.append(current.value)
                current = current.next
        return l
        
    def put_head(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.head is None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        return
            
    def put_tail(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.set_next(node)   
        return
        
    def put_index(self, node, index):
        if not isinstance(node, Node):
            node = Node(node)
        if index > self.get_length():
            raise ValueError('index exceeds length')
        if index == 0:
            current = self.head
            self.head = node
            node.set_next(current)
        else:
            previous = None
            current = self.head
            while index > 0:
                previous = current
                current = current.next
                index -= 1
            node.set_next(current)
            previous.set_next(node)
        return

    def search(self, value):
        i = 0
        l = []
        current = self.head
        while current is not None:
            if current.value == value:
                l.append(i)
            current = current.next
            i += 1
        return l
        
    def delete(self, index):
        if index >= self.get_length():
            raise ValueError('index exceeds length')
        elif index == 0:
            self.head = self.head.next
            return
        else:
            i = 0
            previous = None
            current = self.head
            while i < index:
                i += 1
                previous = current
                current = current.next
            previous.set_next(current.next)
            return
        
    def get_index_value(self, index):
        if index < 0 or index >= self.get_length():
            raise ValueError('index must be between 0 and the length of the linked list')
        i = 0
        current = self.head
        while i < index:
            i += 1
            current = current.next
        return current.value
 