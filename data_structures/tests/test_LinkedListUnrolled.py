import pytest
from ..LinkedListUnrolled import *

#####
# Node
#

@pytest.fixture()
def n():
    n = NodeUnrolled()
    return n

class Test_create_node(object):
    def test_type(self, n):
        assert isinstance(n, NodeUnrolled)
        
    def test_max_elements(self, n):
        assert n.max_elements == 4
        
    def test_num_elements(self, n):
        assert n.num_elements == 0
        
    def test_values(self, n):
        assert n.values == [None, None, None, None]

    def test_next(self, n):
        assert n.next is None
        
class Test_put_node_head(object):
    def test_1(self, n):
        n.put_head(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_head(1)
        n.put_head(2)
        assert n.as_list() == [2, 1]
        assert n.as_list(remove_nones=False) == [2, 1] + [None] * 2
        
    def test_4(self, n):
        n.put_head(1)
        n.put_head(2)
        n.put_head(3)
        n.put_head(4)
        assert n.as_list() == [4, 3, 2, 1]
        assert n.as_list(remove_nones=False) == [4, 3, 2, 1]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_head(i)
        assert 'Node is full' in str(excinfo.value)
        
class Test_put_node_tail(object):
    def test_1(self, n):
        n.put_tail(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_tail(1)
        n.put_tail(2)
        assert n.as_list() == [1, 2]
        assert n.as_list(remove_nones=False) == [1, 2] + [None] * 2
        
    def test_4(self, n):
        n.put_tail(1)
        n.put_tail(2)
        n.put_tail(3)
        n.put_tail(4)
        assert n.as_list() == [1, 2, 3, 4]
        assert n.as_list(remove_nones=False) == [1, 2, 3, 4]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_tail(i)
        assert 'Node is full' in str(excinfo.value)
        
class Test_put_node_index(object):
    def test_1(self, n):
        n.put_index(1, 0)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_index(1, 0)
        n.put_index(2, 0)
        n.put_index(3, 0)
        assert n.as_list() == [3, 2, 1]
        assert n.as_list(remove_nones=False) == [3, 2, 1] + [None]
        
    def test_3(self, n):
        n.put_index(1, 0)
        n.put_index(2, 1)
        n.put_index(3, 2)
        assert n.as_list() == [1, 2, 3]
        assert n.as_list(remove_nones=False) == [1, 2, 3] + [None]
        
    def test_4(self, n):
        n.put_index(1, 0)
        n.put_index(2, 1)
        n.put_index(3, 1)
        n.put_index(4, 2)
        assert n.as_list() == [1, 3, 4, 2]
        assert n.as_list(remove_nones=False) == [1, 3, 4, 2]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_index(i, i)
        assert 'Node is full' in str(excinfo.value)
        
    def test_index_less_than_0(self, n):
        with pytest.raises(IndexError) as excinfo:
            n.put_index(1, -1)
        assert 'Index must be >= 0' in str(excinfo.value)
        
    def test_index_greater_than_max_elements(self, n):
        with pytest.raises(IndexError) as excinfo:
            n.put_index(1, 4)
        assert 'Index exceeds the number of maximum elements' in str(excinfo.value)
        
class Test_put_node_mixed(object):
    def test(self, n):
        n.put_tail(1)
        n.put_tail(2)
        n.put_head(3)
        assert n.as_list() == [3, 1, 2]
        assert n.as_list(remove_nones=False) == [3, 1, 2, None]

#####
# LinkedListUnrolled
#

@pytest.fixture()
def l():
    l = LinkedListUnrolled()
    return l

class Test_create_LinkedListUnrolled(object):
    def test_type(self, l):
        assert isinstance(l, LinkedListUnrolled)
        
    def test_get_head(self, l):
        assert l.get_head() is None
        
    def test_get_tail(self, l):
        assert l.get_tail() is None
        
    def test_get_length(self, l):
        assert l.get_length() == 0
        
    def test_as_list(self, l):
        assert l.as_list() == []

@pytest.fixture()
def l_single():
    l = LinkedListUnrolled()
    l.put_tail(1)
    l.put_tail(2)
    return l

@pytest.fixture()
def l_multiple():
    l = LinkedListUnrolled()
    l.add_node_tail()
    l.put_tail(1)
    l.add_node_tail()
    l.put_tail(2)
    l.put_tail(3)
    l.add_node_tail()
    l.put_tail(4)
    return l

class Test_get_head_and_tail(object):
    def test_get_head_single(self, l_single):
        assert l_single.get_head() == 1
        
    def test_get_tail_single(self, l_single):
        assert l_single.get_tail() == 2
        
    def test_get_head_multiple(self, l_multiple):
        assert l_multiple.get_head() == 1
        
    def test_get_tail_multiple(self, l_multiple):
        assert l_multiple.get_tail() == 4

class Test_get_length(object):
    def test_single(self, l_single):
        assert l_single.get_length() == 2
        
    def test_multiple(self, l_multiple):
        assert l_multiple.get_length() == 4

class Test_as_list(object):
    def test_single(self, l_single):
        assert l_single.as_list() == [1, 2]
        assert l_single.as_list(nested=True) == [[1, 2]]
        assert l_single.as_list(remove_nones = False) == [1, 2, None, None]
        assert l_single.as_list(nested=True, remove_nones=False) == [[1, 2, None, None]]
        
    def test_multiple(self, l_multiple):
        print(vars(l_multiple.head))
        assert l_multiple.as_list() == [1, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1], [2, 3], [4]]
        assert l_multiple.as_list(remove_nones = False) == [1, None, None, None,
                                                            2,    3, None, None,
                                                            4, None, None, None]
        assert l_multiple.as_list(nested=True, remove_nones=False) == [[1, None, None, None],
                                                                       [2,    3, None, None],
                                                                       [4, None, None, None]]

#####
# Put methods
#

def test_all_head():
    l = LinkedListUnrolled()
    l.put_head(1)
    l.put_head(2)
    l.put_head(3)
    l.put_head(4)
    l.put_head(5)
    assert l.as_list() == [5, 4, 3, 2, 1]
    assert l.as_list(nested=True) == [[5, 4, 3, 2], [1]]

def test_all_tail():
    l = LinkedListUnrolled()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    l.put_tail(4)
    l.put_tail(5)
    assert l.as_list() == [1, 2, 3, 4, 5]
    assert l.as_list(nested=True) == [[1, 2, 3, 4], [5]]

def test_mix_head_tail():
    l = LinkedListUnrolled()
    l.put_head(1)
    l.put_tail(2)
    l.put_head(3)
    l.put_tail(4)
    l.put_head(5)
    assert l.as_list() == [5, 3, 1, 2, 4]
    assert l.as_list(nested=True) == [[5, 3, 1, 2], [4]]

#def test_index_empty():
#    l = LinkedListDoubly()
#    l.put_index(1, index=0)
#    assert l.as_list_forward() == [1]
#    assert l.as_list_backward() == [1]
#
#def test_index_head():
#    l = LinkedListDoubly()
#    l.put_head(1)
#    l.put_index(2, index=0)
#    assert l.as_list_forward() == [2, 1]
#    assert l.as_list_backward() == [2, 1]
#
#def test_index_tail():
#    l = LinkedListDoubly()
#    l.put_head(1)
#    l.put_index(2, index=1)
#    assert l.as_list_forward() == [1, 2]
#    assert l.as_list_backward() == [1, 2]
#
#def test_mix_all():
#    l = LinkedListDoubly()
#    l.put_head(1)
#    l.put_tail(2)
#    l.put_index(3, index=1)
#    l.put_head(4)
#    l.put_tail(5)
#    l.put_index(6, index=3)
#    assert l.as_list_forward() == [4, 1, 3, 6, 2, 5]
#    assert l.as_list_backward() == [4, 1, 3, 6, 2, 5]
#
#def test_put_index_gt_0():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.put_index(1, index=-1)
#    assert 'index must be >= 0' in str(excinfo.value)
#
#def test_put_index_gt_length():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.put_index(1, index=1)
#    assert 'index exceeds list length' in str(excinfo.value)
#    
######
## Get index value
##
#
#def test_get_value_index_value_low():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.get_value_index(0)
#    assert 'list is empty' in str(excinfo.value)
#
#def test_get_value_index_value_high():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.put_tail(1)
#        l.get_value_index(1)
#    assert 'index exceeds list length' in str(excinfo.value)
#    
#def test_get_value_index_head():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    assert l.get_value_index(0) == 1
#    
#def test_get_value_index_tail():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    assert l.get_value_index(2) == 3
#    
#def test_get_value_index_middle():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    assert l.get_value_index(1) == 2
#
######
## Search
##
#
#def test_search_empty_list():
#    l = LinkedListDoubly()
#    assert l.search(1) == []
#
#def test_search_no_matches():
#    l = LinkedListDoubly()
#    l.put_head(2)
#    l.put_head(3)
#    assert l.search(1) == []
#
#def test_search_one_match():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    assert l.search(1) == [0]
#
#def test_search_two_matches():
#    l = LinkedListDoubly()
#    l.put_tail(2)
#    l.put_tail(1)
#    l.put_tail(3)
#    l.put_tail(1)
#    assert l.search(1) == [1, 3]
#    
######
## Delete
##
#
#def test_delete_index_empty():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.delete(0)
#    assert 'list is empty' in str(excinfo.value)
#
#def test_delete_index_gt_length():
#    with pytest.raises(ValueError) as excinfo:
#        l = LinkedListDoubly()
#        l.put_tail(1)
#        l.put_tail(2)
#        l.delete(5)
#    assert 'index exceeds list length' in str(excinfo.value)
#    
#def test_delete_single_node():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.delete(0)
#    assert l.as_list_forward() == []
#    assert l.as_list_backward() == []
#
#def test_delete_head():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.delete(0)
#    assert l.as_list_forward() == [2]
#    assert l.as_list_backward() == [2]
#
#def test_delete_tail():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.delete(1)
#    assert l.as_list_forward() == [1]
#    assert l.as_list_backward() == [1]
#
#def test_delete_middle():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    l.delete(1)
#    assert l.as_list_forward() == [1, 3]
#    assert l.as_list_backward() == [1, 3]
#
#def test_delete_multiple():
#    l = LinkedListDoubly()
#    l.put_tail(1)
#    l.put_tail(2)
#    l.put_tail(3)
#    l.put_tail(4)
#    l.put_tail(5)
#    l.put_tail(6)
#    l.delete(0)
#    l.delete(2)
#    l.delete(3)
#    assert l.as_list_forward() == [2, 3, 5]
#    assert l.as_list_backward() == [2, 3, 5]
