class NodeUnrolled:
    def __init__(self, max_elements=4, next=None):
        self.max_elements = max_elements
        self.num_elements = 0
        self.values = [None] * self.max_elements
        self.next = next
        return
        
    def put_head(self, value):
        """Adds value at the head of values"""
        if self.num_elements == self.max_elements:
            raise IndexError('node is full')
        self.values = [value] + self.values[:self.max_elements - 1]
        self.num_elements += 1
        return
        
    def put_tail(self, value):
        """Adds value at the tail of values"""
        if self.num_elements == self.max_elements:
            raise IndexError('node is full')
        self.values[self.num_elements] = value
        self.num_elements += 1
        return
        
    def put_index(self, value, index):
        """Adds value at the specified index of values"""
        if self.num_elements == self.max_elements:
            raise IndexError('node is full')
        elif index < 0:
            raise IndexError('index must be >= 0')
        elif index >= self.max_elements:
            raise IndexError('index exceeds the number of maximum elements')
        index = int(index)
        if index == 0:
            self.put_head(value)
        elif index < self.num_elements:
            self.values = self.values[:index] + [value] + self.values[index:self.max_elements - 1]
            self.num_elements += 1
        elif index == self.num_elements:
            self.put_tail(value)
        else:
            raise IndexError('index exceeds number of elements in the node')
        return
        
    def pop_tail(self):
        """Removes and returns the tail of values"""
        self.num_elements -= 1
        val = self.values.pop()
        self.values += [None]
        return val
        
    def delete(self, index):
        """Removes value at the specified index"""
        if index < 0:
            raise IndexError('index must be >= 0')
        elif index >= self.num_elements:
            raise IndexError('index exceeds the number of elements')
        index = int(index)
        self.values = [self.values[i] for i in range(self.max_elements) if i != index] + [None]
        self.num_elements -= 1
        return
        
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
            current = self.head 
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = NodeUnrolled()
        return
        
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
        
    def get_index(self, index):
        if index < 0:
            raise IndexError('index must be >= 0')
        if index == 0:
            val = self.get_head()
        else:
            current = self.head
            val = self._get_index(index, current)
        return val 
        
    def _get_index(self, index, current_node):
        if index < current_node.num_elements:
            return current_node.values[index]
        else:
            if current_node.next is None:
                raise IndexError('index exceeds list length')
            index -= current_node.num_elements
            current_node = current_node.next
            val = self._get_index(index, current_node)
        return val
            
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
        """Adds value to the beginning of the list (specifically the start of the head node)"""
        if self.head is None:
            self.head = NodeUnrolled()
        current = self.head
        self._put_head(value, current)
        return
        
    def _put_head(self, value, current_node):
        try:
            current_node.put_head(value)
        except IndexError:
            value_for_next_node = current_node.pop_tail()
            current_node.put_head(value)
            if current_node.next is None:
                current_node.next = NodeUnrolled()
            self._put_head(value_for_next_node, current_node.next)
        return
        
    def put_tail(self, value):
        """Adds value to the end of the list (specifically the end of the tail node)"""
        if self.head is None:
            self.head = NodeUnrolled()
        current = self.head
        while current.next is not None:
            current = current.next
        self._put_tail(value, current)
        return
        
    def _put_tail(self, value, current_node):
        try:
            current_node.put_tail(value)
        except IndexError:
            current_node.next = NodeUnrolled()
            current_node.next.put_tail(value)
        return
        
    def put_index(self, value, index):
        """Adds value at the specified index of the list"""
        if index < 0:
            raise IndexError('index must be >= 0')
        if index == 0:
            val = self.put_head(value)
        elif index == self.get_length():
            val = self.put_tail(value)
        else:
            current = self.head
            self._put_index(value, index, current)        
        return
        
    def _put_index(self, value, index, current_node):
        if index <= current_node.num_elements and index < current_node.max_elements:
            try:
                current_node.put_index(value, index)
            except IndexError:
                self._overflow_to_next_node(value, index, current_node)
        else:
            if current_node.next is None:
                raise IndexError('index exceeds list length')
            index -= current_node.num_elements
            current_node = current_node.next
            self._put_index(value, index, current_node)
        return
        
    def _overflow_to_next_node(self, value, index, current_node):
        value_to_transfer = current_node.pop_tail()
        current_node.put_index(value, index)
        if current_node.next is None:
            current_node.next = NodeUnrolled()
        try:
            current_node.next.put_head(value_to_transfer)
        except IndexError:
            self._overflow_to_next_node(value_to_transfer, 0, current_node.next)
        return
        
    def search(self, value):
        """Searches for value in the list and returns all indices that match,
           returns an empty list if no matches are found"""
        i = 0
        l = []
        current = self.head
        while current is not None:
            for v in current.values:
                if v is None:
                    break
                elif v == value:
                    l += [i]
                i += 1
            current = current.next
        return l
        
    def delete(self, index):
        """Deletes the value at the given index"""
        if self.get_length() == 0:
            raise ValueError('list is empty')
        elif index < 0:
            raise IndexError('index must be >= 0')
        current = self.head
        self._delete(index, current)
        return
        
    def _delete(self, index, current_node):
        if index < current_node.num_elements:
            current_node.delete(index)
        else:
            if current_node.next is None:
                raise IndexError('index exceeds list length')
            index -= current_node.num_elements
            self._delete(index, current_node.next)
        return
