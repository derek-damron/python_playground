import pytest
from LinkedListSingly import *

#####
# Node
#

@pytest.fixture()
def n():
    n = Node(0)
    return n

class Test_create_node(object):
    def test_type(self, n):
        assert isinstance(n, Node)
        
    def test_value(self, n):
        assert n.value == 0

    def test_next(self, n):
        assert n.next is None
                
    def test_set_value(self, n):
        n.set_value(1)
        assert n.value == 1
        
    def test_set_next(self, n):
        a = Node(2)
        n.set_next(a)
        assert n.next == a
        
#####
# LinkedListSingly
#

@pytest.fixture()
def l():
    l = LinkedListSingly()
    return l

class Test_create_LinkedListSingly(object):
    def test_type(self, l):
        assert isinstance(l, LinkedListSingly)
        
    def test_get_head(self, l):
        assert l.head is None
        
    def test_get_tail(self, l):
        assert l.get_tail() is None

@pytest.fixture()
def l2():
    l = LinkedListSingly()
    l.put_head(1)
    l.put_head(2)
    return l

class Test_get_head_and_tail(object):
    def test_get_head(self, l2):
        assert l2.head.value == 2
        
    def test_get_tail(self, l2):
        assert l2.get_tail().value == 1
        
class Test_get_length(object):
    def test_length_0(self):
        l = LinkedListSingly()
        assert l.get_length() == 0
        
    def test_length_1(self):
        l = LinkedListSingly()
        l.put_head(1)
        assert l.get_length() == 1
        
    def test_length_2(self):
        l = LinkedListSingly()
        l.put_head(1)
        l.put_head(2)
        assert l.get_length() == 2
        
    def test_length_5(self):
        l = LinkedListSingly()
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
    l = LinkedListSingly()
    l.put_head(1)
    l.put_head(2)
    l.put_head(3)
    assert l.as_list() == [3, 2, 1]

def test_all_tail():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.as_list() == [1, 2, 3]

def test_mix_head_tail():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_head(2)
    l.put_tail(3)
    assert l.as_list() == [2, 1, 3]

def test_index_empty():
    l = LinkedListSingly()
    l.put_index(1, index=0)
    assert l.as_list() == [1]

def test_index_head():
    l = LinkedListSingly()
    l.put_head(1)
    l.put_index(2, index=0)
    assert l.as_list() == [2, 1]

def test_index_tail():
    l = LinkedListSingly()
    l.put_head(1)
    l.put_index(2, index=1)
    assert l.as_list() == [1, 2]

def test_mix_all():
    l = LinkedListSingly()
    l.put_head(1)
    l.put_tail(2)
    l.put_index(3, index=1)
    l.put_head(4)
    l.put_tail(5)
    l.put_index(6, index=3)
    assert l.as_list() == [4, 1, 3, 6, 2, 5]

def test_put_index_gt_length():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListSingly()
        l.put_index(1, index=1)
    assert 'index exceeds length' in str(excinfo.value)
    
#####
# Search
#

def test_search_no_matches():
    l = LinkedListSingly()
    l.put_head(2)
    l.put_head(3)
    assert l.search(1) == []

def test_search_one_match():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.search(1) == [0]

def test_search_two_matches():
    l = LinkedListSingly()
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
        l = LinkedListSingly()
        l.delete(0)
    assert 'index exceeds length' in str(excinfo.value)
    
def test_delete_single_node():
    l = LinkedListSingly()
    l.put_tail(1)
    l.delete(0)
    assert l.as_list() == []

def test_delete_head():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.delete(0)
    assert l.as_list() == [2]

def test_delete_tail():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.delete(1)
    assert l.as_list() == [1]

def test_delete_middle():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    l.delete(1)
    assert l.as_list() == [1, 3]
    
#####
# Get index value
#

def test_get_index_value_value_low():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListSingly()
        l.get_index_value(0)
    assert 'index must be between 0 and the length of the linked list' in str(excinfo.value)

def test_get_index_value_value_high():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListSingly()
        l.put_tail(1)
        l.get_index_value(1)
    assert 'index must be between 0 and the length of the linked list' in str(excinfo.value)
    
def test_get_index_value_head():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_index_value(0) == 1
    
def test_get_index_value_tail():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_index_value(2) == 3
    
def test_get_index_value_middle():
    l = LinkedListSingly()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    assert l.get_index_value(1) == 2