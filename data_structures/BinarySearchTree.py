class NodeBinarySearchTree(object):
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
        return
        
class BinarySearchTree(object):
    def __init__(self):
        self._root = None
        return
        
    def insert(self, value):
        new_node = NodeBinarySearchTree(value)
        if self._root is None:
            self._root = new_node
        else:
            self._insert(new_node, self._root)
        return
            
    def _insert(self, new_node, current_node):
        if new_node._value == current_node._value:
            raise ValueError("value already exists")
        elif new_node._value < current_node._value:
            if current_node._left is None:
                current_node._left = new_node
            else:
                self._insert(new_node, current_node._left)
        else:
            if current_node._right is None:
                current_node._right = new_node
            else:
                self._insert(new_node, current_node._right)
        return
        
    def as_list(self):
        if self._root is None:
            return []
        return self._as_list(self._root, [])
            
    def _as_list(self, current_node, current_list):
        # Return left-hand stuff if exists
        if current_node._left is not None:
            self._as_list(current_node._left, current_list)
        # Return current
        current_list += [current_node._value]
        # Return right-hand stuff if exists
        if current_node._right is not None:
            self._as_list(current_node._right, current_list)
        return current_list
        
    def print_as_tree(self):
        if self._root is None:
            return ""
        self._print_as_tree(self._root, 0)
        return
        
    def _print_as_tree(self, current_node, left_buffer):
        if current_node._right is not None:
            self._print_as_tree(current_node._right, left_buffer + len(str(current_node._value)))
        print(" " * left_buffer + str(current_node._value))
        if current_node._left is not None:
            self._print_as_tree(current_node._left, left_buffer + len(str(current_node._value)))
        return
        
    def get_height(self):
        if self._root is None:
            return 0
        return self._get_height(self._root, 1)
        
    def _get_height(self, current_node, current_height):
        # Traverse left if exists
        if current_node._left is not None:
            left_height = self._get_height(current_node._left, current_height + 1)
        else:
            left_height = current_height
        # Traverse right if exists
        if current_node._right is not None:
            right_height = self._get_height(current_node._right, current_height + 1)
        else:
            right_height = current_height
        return max(left_height, right_height)
        
    def search(self, value):
        if self._root is None:
            return False
        return self._search(value, self._root)
        
    def _search(self, value, current_node):
        if value == current_node._value:
            return True
        elif value < current_node._value:
            if current_node._left is None:
                return False
            return self._search(value, current_node._left)
        else:
            if current_node._right is None:
                return False
            return self._search(value, current_node._right)
                        
    def delete(self, value):
        if self._root is None:
            return
        return self._delete(value, self._root, None)
    
    def _delete(self, value, current_node, parent):
        if value < current_node._value:
            self._delete(value, current_node._left, current_node)
        elif value > current_node._value:
            self._delete(value, current_node._right, current_node)
        if value == current_node._value:
            # If no children then delete
            if current_node._left is None and current_node._right is None:
                if current_node == parent._left:
                    parent._left = None
                else:
                    parent._right = None
            # If only one child then replace with that child
            elif current_node._left is None:
                if current_node == parent._left:
                    parent._left = current_node._right
                else:
                    parent._right = current_node._right
            elif current_node._right is None:
                if current_node == parent._left:
                    parent._left = current_node._left
                else:
                    parent._right = current_node._left
            # If two children then get the next highest value by finding the min of the right subtree
            else:
                replacement_node = self.find_min(current_node._right)
                current_node._value = replacement_node._value
                self._delete(replacement_node._value, current_node._right, current_node)
        return
            
    def find_min(self, current_node):
        while current_node._left is not None:
            current_node = current_node._left
        return current_node
                                
    def rebalance(self):
        if self._root is None:
            return
        values = self.as_list()
        new_tree = BinarySearchTree()
        self._rebalance(new_tree, values)
        self._root = new_tree._root
        return
    
    def _rebalance(self, new_tree, values):
        if len(values) == 1:
            new_tree.insert(values[0])
        elif len(values) > 1:
            # Insert middle value
            middle_value_index = int(len(values) / 2)
            new_tree.insert(values[middle_value_index])
            # Recurse over values left of middle value
            values_left = values[:middle_value_index]
            self._rebalance(new_tree, values_left)
            # Recurse over values right of middle value
            values_right = values[(middle_value_index + 1):]
            self._rebalance(new_tree, values_right)
        return
        
