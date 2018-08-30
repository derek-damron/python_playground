class NodeUnrolled:
    def __init__(self, max_elements=4, next=None):
        self.max_elements = max_elements
        self.num_elements = 0
        self.values = [None] * self.max_elements
        self.next = next
        return
        
    def put_head(self, value):
        """Puts value at the head of values"""
        if self.num_elements == self.max_elements:
            raise IndexError('Node is full')
        self.values = [value] + self.values[:self.max_elements - 1]
        self.num_elements += 1
        return
        
    def put_tail(self, value):
        """Puts value at the tail of values"""
        if self.num_elements == self.max_elements:
            raise IndexError('Node is full')
        self.values[self.num_elements] = value
        self.num_elements += 1
        return
        
    def put_index(self, value, index):
        pass
        
    def as_list(self, remove_nones=True):
        if remove_nones:
            return [i for i in self.values if i is not None]
        else:
            return self.values

class LinkedListUnrolled:
    def __init__(self, head=None):
        self.head = None
        return
        
    def add_node_tail(self):
        if self.head is None:
            self.head = NodeUnrolled()
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = NodeUnrolled()            
        
    def get_head(self):
        """Get the first value"""
        if self.head is None:
            return self.head
        return self.head.values[0]
            
    def get_tail(self):
        """Get the last value"""
        if self.head is None:
            return self.head
        current = self.head
        while current.next is not None:
            current = current.next
        return current.values[current.num_elements - 1]
            
    def get_length(self):
        """Get the length of the list"""
        current = self.head
        i = 0
        while current is not None:
            i += current.num_elements
            current = current.next
        return i
            
    def as_list(self, nested=False, remove_nones=True):
        """Returns the node values as a Python list"""
        l = []
        if self.head is not None:
            current = self.head
            while current is not None:
                if nested:
                    l += [current.as_list(remove_nones)]
                else:
                    l += current.as_list(remove_nones)
                current = current.next
        return l
        
    def put_head(self, value):
        pass
        
    def put_tail(self, value):
        """Adds value to the end of the tail node"""
        if self.head is None:
            self.head = NodeUnrolled()
        current = self.head
        while current.next is not None:
            current = current.next
        try:
            current.put_tail(value)
        except IndexError:
            current.next = NodeUnrolled()
            current.next.put_tail(value)
        return
            