import pytest
from BinarySearchTree import *

#####
# Node
#

@pytest.fixture()
def n():
    n = NodeBinarySearchTree(0)
    return n

class Test_create_node(object):
    def test_type(self, n):
        assert isinstance(n, NodeBinarySearchTree)
        
    def test_value(self, n):
        assert n._value == 0

    def test_left(self, n):
        assert n._left is None

    def test_right(self, n):
        assert n._right is None
        
#####
# BinarySearchTree
#

@pytest.fixture()
def b():
    b = BinarySearchTree()
    return b

class Test_create_BinarySearchTree(object):
    def test_type(self, b):
        assert isinstance(b, BinarySearchTree)
        
    def test_root(self, b):
        assert b._root is None

#####
# as_list, print_as_tree, and get_height for empty tree
#

class Test_list_print_and_height(object):
    def test_empty_tree(self, capsys):
        b = BinarySearchTree()
        assert b.get_height() == 0
        assert b.as_list() == []
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ''
        
#####
# Insert
#

class Test_insert(object):
    def test_insert_root(self, capsys):
        b = BinarySearchTree()
        b.insert(1)
        assert b.get_height() == 1
        assert b.as_list() == [1]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == '1' + '\n'
        
    def test_insert_both_sides(self, capsys):
        b = BinarySearchTree()
        b.insert(2)
        b.insert(1)
        b.insert(3)
        assert b.get_height() == 2
        assert b.as_list() == [1, 2, 3]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == (' 3' + '\n' + 
                       '2' + '\n' +
                       ' 1' + '\n')
        
    def test_insert_complete_tree(self, capsys):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(3)
        b.insert(4)
        b.insert(2)
        b.insert(8)
        b.insert(9)
        b.insert(7)
        assert b.get_height() == 3
        assert b.as_list() == [2, 3, 4, 5, 7, 8, 9]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('  9' + '\n' + 
                       ' 8' + '\n' + 
                       '  7' + '\n' + 
                       '5' + '\n' +
                       '  4' + '\n' + 
                       ' 3' + '\n' + 
                       '  2' + '\n')
        
    def test_insert_imbalanced_tree(self, capsys):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(4)
        b.insert(3)
        b.insert(2)
        b.insert(7)
        b.insert(8)
        b.insert(9)
        assert b.get_height() == 4
        assert b.as_list() == [2, 3, 4, 5, 7, 8, 9]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('   9' + '\n' + 
                       '  8' + '\n' + 
                       ' 7' + '\n' + 
                       '5' + '\n' +
                       ' 4' + '\n' + 
                       '  3' + '\n' + 
                       '   2' + '\n')
        
    def test_insert_existing_value(self):
        with pytest.raises(ValueError) as excinfo:
            b = BinarySearchTree()
            b.insert(1)
            b.insert(1)
        assert 'value already exists' in str(excinfo.value)

#####
# Search
#

class Test_search(object):
    def test_empty_tree(self):
        b = BinarySearchTree()
        assert not b.search(1)
        
    def test_value_in_tree(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(4)
        b.insert(3)
        b.insert(2)
        b.insert(7)
        b.insert(8)
        b.insert(9)
        assert b.search(5)
        assert b.search(2)
        assert b.search(9)
        
    def test_value_not_in_tree(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(4)
        b.insert(3)
        b.insert(2)
        b.insert(7)
        b.insert(8)
        b.insert(9)
        assert not b.search(1)
        assert not b.search(10)
    
#####
# Delete
#

class Test_delete(object):
    def test_empty_tree(self):
        b = BinarySearchTree()
        assert not b.delete(1)
                
    def test_no_children(self, capsys):
        b = BinarySearchTree()
        b.insert(2)
        b.insert(3)
        b.insert(1)
        b.delete(3)
        b.delete(1)
        assert b.as_list() == [2]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('2' + '\n')
                
    def test_one_child(self, capsys):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(5-3)
        b.insert(5-4)
        b.insert(5-5)
        b.insert(5-1)
        b.insert(5-2)
        b.insert(5+3)
        b.insert(5+4)
        b.insert(5+5)
        b.insert(5+1)
        b.insert(5+2)
        b.delete(5-4)
        b.delete(5-1)
        b.delete(5+1)
        b.delete(5+4)
        assert b.as_list() == [0, 2, 3, 5, 7, 8, 10]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('  10' + '\n' +
                       ' 8' + '\n' +
                       '  7' + '\n' +
                       '5' + '\n' +
                       '  3' + '\n' + 
                       ' 2' + '\n' + 
                       '  0' + '\n')
                
    def test_two_children(self, capsys):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(5-3)
        b.insert(5-4)
        b.insert(5-5)
        b.insert(5-1)
        b.insert(5-2)
        b.insert(5+3)
        b.insert(5+4)
        b.insert(5+5)
        b.insert(5+1)
        b.insert(5+2)
        b.delete(5)
        assert b.as_list() == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('   10' + '\n' +
                       '  9' + '\n' +
                       ' 8' + '\n' +
                       '  7' + '\n' +
                       '6' + '\n' +
                       '  4' + '\n' +
                       '   3' + '\n' + 
                       ' 2' + '\n' + 
                       '  1' + '\n' + 
                       '   0' + '\n')    

#####
# Rebalance
#

class Test_rebalance(object):
    def test_empty_tree(self):
        b = BinarySearchTree()
        assert not b.rebalance()
                
    def test_unbalanced(self, capsys):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(5-3)
        b.insert(5-4)
        b.insert(5-5)
        b.insert(5-1)
        b.insert(5-2)
        b.insert(5+3)
        b.insert(5+4)
        b.insert(5+5)
        b.insert(5+1)
        b.insert(5+2)
        assert b.as_list() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('   10' + '\n' +
                       '  9' + '\n' +
                       ' 8' + '\n' +
                       '   7' + '\n' +
                       '  6' + '\n' +
                       '5' + '\n' +
                       '  4' + '\n' +
                       '   3' + '\n' + 
                       ' 2' + '\n' + 
                       '  1' + '\n' + 
                       '   0' + '\n')  
        b.rebalance()
        assert b.as_list() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        b.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('  10' + '\n' +
                       '    9' + '\n' +
                       ' 8' + '\n' +
                       '  7' + '\n' +
                       '   6' + '\n' +
                       '5' + '\n' +
                       '  4' + '\n' +
                       '   3' + '\n' + 
                       ' 2' + '\n' + 
                       '  1' + '\n' + 
                       '   0' + '\n')  
#####
# Verify
#

@pytest.fixture()
def bv():
    bv = BinarySearchTree()
    bv.insert(5)
    bv.insert(3)
    bv.insert(4)
    bv.insert(2)
    bv.insert(7)
    bv.insert(8)
    bv.insert(6)
    return bv

class Test_verify(object):
    def test_empty_tree(self, bv):
        b = BinarySearchTree()
        assert not b.verify()
                
    def test_corret(self, bv):
        assert bv.verify()
                
    def test_incorrect_left(self, bv):
        bv._root._left._value = 10
        assert not bv.verify()
                
    def test_incorrect_left_left(self, bv):
        bv._root._left._left._value = 10
        assert not bv.verify()
                
    def test_incorrect_right(self, bv):
        bv._root._right._value = 0
        assert not bv.verify()
                
    def test_incorrect_right_right(self, bv):
        bv._root._right._right._value = 0
        assert not bv.verify()