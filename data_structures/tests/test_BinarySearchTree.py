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
        l = BinarySearchTree()
        assert l.get_height() == 0
        assert l.as_list() == []
        l.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ''
        
#####
# Insert
#

class Test_insert(object):
    def test_insert_root(self, capsys):
        l = BinarySearchTree()
        l.insert(1)
        assert l.get_height() == 1
        assert l.as_list() == [1]
        l.print_as_tree()
        out, err = capsys.readouterr()
        assert out == '1' + '\n'
        
    def test_insert_both_sides(self, capsys):
        l = BinarySearchTree()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        assert l.get_height() == 2
        assert l.as_list() == [1, 2, 3]
        l.print_as_tree()
        out, err = capsys.readouterr()
        assert out == (' 3' + '\n' + 
                       '2' + '\n' +
                       ' 1' + '\n')
        
    def test_insert_complete_tree(self, capsys):
        l = BinarySearchTree()
        l.insert(5)
        l.insert(3)
        l.insert(4)
        l.insert(2)
        l.insert(8)
        l.insert(9)
        l.insert(7)
        assert l.get_height() == 3
        assert l.as_list() == [2, 3, 4, 5, 7, 8, 9]
        l.print_as_tree()
        out, err = capsys.readouterr()
        assert out == ('  9' + '\n' + 
                       ' 8' + '\n' + 
                       '  7' + '\n' + 
                       '5' + '\n' +
                       '  4' + '\n' + 
                       ' 3' + '\n' + 
                       '  2' + '\n')
        
    def test_insert_imbalanced_tree(self, capsys):
        l = BinarySearchTree()
        l.insert(5)
        l.insert(4)
        l.insert(3)
        l.insert(2)
        l.insert(7)
        l.insert(8)
        l.insert(9)
        assert l.get_height() == 4
        assert l.as_list() == [2, 3, 4, 5, 7, 8, 9]
        l.print_as_tree()
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
            l = BinarySearchTree()
            l.insert(1)
            l.insert(1)
        assert 'value already exists' in str(excinfo.value)

#####
# Search
#

class Test_search(object):
    def test_empty_tree(self, capsys):
        l = BinarySearchTree()
        assert not l.search(1)
        
    def test_value_in_tree(self, capsys):
        l = BinarySearchTree()
        l.insert(5)
        l.insert(4)
        l.insert(3)
        l.insert(2)
        l.insert(7)
        l.insert(8)
        l.insert(9)
        assert l.search(5)
        assert l.search(2)
        assert l.search(9)
        
    def test_value_not_in_tree(self, capsys):
        l = BinarySearchTree()
        l.insert(5)
        l.insert(4)
        l.insert(3)
        l.insert(2)
        l.insert(7)
        l.insert(8)
        l.insert(9)
        assert not l.search(1)
        assert not l.search(10)
    