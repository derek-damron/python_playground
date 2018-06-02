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
