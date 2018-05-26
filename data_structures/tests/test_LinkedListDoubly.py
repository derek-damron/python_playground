import pytest
from LinkedListDoubly import *

#####
# Node
#

@pytest.fixture()
def n():
    n = NodeDoubly(0)
    return n

class Test_create_node(object):
    def test_type(self, n):
        assert isinstance(n, NodeDoubly)
        
    def test_value(self, n):
        assert n._value == 0

    def test_next(self, n):
        assert n._next is None

    def test_prev(self, n):
        assert n._prev is None
                
    def test_set_value(self, n):
        n.set_value(1)
        assert n._value == 1
        
    def test_set_next(self, n):
        a = NodeDoubly(2)
        n.set_next(a)
        assert n._next == a
        
    def test_set_prev(self, n):
        a = NodeDoubly(2)
        n.set_next(a)
        assert n._next == a
        
#####
# LinkedListDoubly
#

@pytest.fixture()
def l():
    l = LinkedListDoubly()
    return l

class Test_create_LinkedListDoubly(object):
    def test_type(self, l):
        assert isinstance(l, LinkedListDoubly)
        
    def test_get_head(self, l):
        assert l._head is None
        
    def test_get_tail(self, l):
        assert l._tail is None

@pytest.fixture()
def l2():
    l = LinkedListDoubly()
    l.put_head(1)
    l.put_head(2)
    return l

class Test_get_head_and_tail(object):
    def test_get_head(self, l2):
        assert l2._head._value == 2
        
    def test_get_tail(self, l2):
        assert l2._tail._value == 1
        
class Test_get_length(object):
    def test_length_0(self):
        l = LinkedListDoubly()
        assert l.get_length() == 0
        
    def test_length_1(self):
        l = LinkedListDoubly()
        l.put_head(1)
        assert l.get_length() == 1
        
    def test_length_2(self):
        l = LinkedListDoubly()
        l.put_head(1)
        l.put_head(2)
        assert l.get_length() == 2
        
    def test_length_5(self):
        l = LinkedListDoubly()
        l.put_head(1)
        l.put_head(2)
        l.put_head(3)
        l.put_head(4)
        l.put_head(5)
        assert l.get_length() == 5
        
#####
# Put methods
#

def test_all_head():
    l = LinkedListDoubly()
    l.put_head(1)
    l.put_head(2)
    l.put_head(3)
    assert l.as_list_forward() == [3, 2, 1]
    assert l.as_list_backward() == [3, 2, 1]

def test_all_tail():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.as_list_forward() == [1, 2, 3]
    assert l.as_list_backward() == [1, 2, 3]

def test_mix_head_tail():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_head(2)
    l.put_tail(3)
    assert l.as_list_forward() == [2, 1, 3]
    assert l.as_list_backward() == [2, 1, 3]

def test_index_empty():
    l = LinkedListDoubly()
    l.put_index(1, index=0)
    assert l.as_list_forward() == [1]
    assert l.as_list_backward() == [1]

def test_index_head():
    l = LinkedListDoubly()
    l.put_head(1)
    l.put_index(2, index=0)
    assert l.as_list_forward() == [2, 1]
    assert l.as_list_backward() == [2, 1]

def test_index_tail():
    l = LinkedListDoubly()
    l.put_head(1)
    l.put_index(2, index=1)
    assert l.as_list_forward() == [1, 2]
    assert l.as_list_backward() == [1, 2]

def test_mix_all():
    l = LinkedListDoubly()
    l.put_head(1)
    l.put_tail(2)
    l.put_index(3, index=1)
    l.put_head(4)
    l.put_tail(5)
    l.put_index(6, index=3)
    assert l.as_list_forward() == [4, 1, 3, 6, 2, 5]
    assert l.as_list_backward() == [4, 1, 3, 6, 2, 5]

def test_put_index_gt_0():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.put_index(1, index=-1)
    assert 'index must be >= 0' in str(excinfo.value)

def test_put_index_gt_length():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.put_index(1, index=1)
    assert 'index exceeds list length' in str(excinfo.value)
    
#####
# Get index value
#

def test_get_value_index_value_low():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.get_value_index(0)
    assert 'list is empty' in str(excinfo.value)

def test_get_value_index_value_high():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.put_tail(1)
        l.get_value_index(1)
    assert 'index exceeds list length' in str(excinfo.value)
    
def test_get_value_index_head():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_value_index(0) == 1
    
def test_get_value_index_tail():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_value_index(2) == 3
    
def test_get_value_index_middle():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_value_index(1) == 2

#####
# Search
#

def test_search_empty_list():
    l = LinkedListDoubly()
    assert l.search(1) == []

def test_search_no_matches():
    l = LinkedListDoubly()
    l.put_head(2)
    l.put_head(3)
    assert l.search(1) == []

def test_search_one_match():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.search(1) == [0]

def test_search_two_matches():
    l = LinkedListDoubly()
    l.put_tail(2)
    l.put_tail(1)
    l.put_tail(3)
    l.put_tail(1)
    assert l.search(1) == [1, 3]
    
#####
# Delete
#

def test_delete_index_gt_length():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.delete(0)
    assert 'list is empty' in str(excinfo.value)

def test_delete_index_gt_length():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListDoubly()
        l.put_tail(1)
        l.put_tail(2)
        l.delete(5)
    assert 'index exceeds list length' in str(excinfo.value)
    
def test_delete_single_node():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.delete(0)
    assert l.as_list_forward() == []
    assert l.as_list_backward() == []

def test_delete_head():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.delete(0)
    assert l.as_list_forward() == [2]
    assert l.as_list_backward() == [2]

def test_delete_tail():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.delete(1)
    assert l.as_list_forward() == [1]
    assert l.as_list_backward() == [1]

def test_delete_middle():
    l = LinkedListDoubly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    l.delete(1)
    assert l.as_list_forward() == [1, 3]
    assert l.as_list_backward() == [1, 3]
