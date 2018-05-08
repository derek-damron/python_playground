class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        return
        
    def set_value(self, value):
        """Set the value of the node"""
        self.value = value
        return
        
    def set_next(self, next):
        """Set the next node in the list"""
        self.next = next
        return
        
class LinkedListSingly:
    def __init__(self, head=None):
        self.head = head
        return
        
    def get_tail(self):
        """Get the last node"""
        if self.head is None:
            return self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current
            
    def get_length(self):
        """Get the length of the list"""
        current = self.head
        i = 0
        while current is not None:
            i += 1
            current = current.next
        return i
        
    def as_list(self):
        """Return the node values as a Python list"""
        l = []
        if self.head is not None:
            current = self.head
            while current is not None:
                l.append(current.value)
                current = current.next
        return l
        
    def put_head(self, node):
        """Insert a new node at the head"""
        if not isinstance(node, Node):
            node = Node(node)
        if self.head is None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        return
            
    def put_tail(self, node):
        """Insert a new node at the tail"""
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
        """Insert a new node at the specified index"""
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
        """Search the list for a particular value, will return all instances that match"""
        i = 0
        l = []
        current = self.head
        while current is not None:
            if current.value == value:
                l.append(i)
            current = current.next
            i += 1
        return l
        
    def delete_head(self):
        """Delete the head node"""
        self.delete_index(0)
        return
        
    def delete_tail(self):
        """Delete the tail node"""
        self.delete_index(self.get_length() - 1)
        return
        
    def delete_index(self, index):
        """Delete the node at a specific index"""
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
        
    def get_value_index(self, index):
        """Get the node value at a specific index"""
        if index < 0 or index >= self.get_length():
            raise ValueError('index must be between 0 and the length of the linked list')
        i = 0
        current = self.head
        while i < index:
            i += 1
            current = current.next
        return current.value
 