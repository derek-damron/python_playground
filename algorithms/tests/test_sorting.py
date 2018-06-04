import pytest
from ..sorting import *
import random

@pytest.fixture()
def l_empty():
    return []

class Test_empty_list(object):
    def test_insertion(self, l_empty):
        assert insertion_sort(l_empty) == []
        
    def test_bubble(self, l_empty):
        assert bubble_sort(l_empty) == []
        
    def test_selection(self, l_empty):
        assert selection_sort(l_empty) == []
        
    def test_quick(self, l_empty):
        assert quicksort(l_empty) == []

@pytest.fixture()
def l_single():
    return [1]

class Test_singleton_list(object):
    def test_insertion(self, l_single):
        assert insertion_sort(l_single) == [1]
        
    def test_bubble(self, l_single):
        assert bubble_sort(l_single) == [1]
        
    def test_selection(self, l_single):
        assert selection_sort(l_single) == [1]
        
    def test_quick(self, l_single):
        assert quicksort(l_single) == [1]

@pytest.fixture()
def l_expected():
    return [x for x in range(20)]

class Test_ordered_list(object):
    def test_insertion(self, l_expected):
        assert insertion_sort(l_expected) == l_expected
        
    def test_bubble(self, l_expected):
        assert bubble_sort(l_expected) == l_expected
        
    def test_selection(self, l_expected):
        assert selection_sort(l_expected) == l_expected
        
    def test_quick(self, l_expected):
        assert quicksort(l_expected) == l_expected

@pytest.fixture()
def l_reversed():
    return [x for x in range(20)][::-1]

class Test_reversed_list(object):
    def test_insertion(self, l_reversed, l_expected):
        assert insertion_sort(l_reversed) == l_expected
        
    def test_bubble(self, l_reversed, l_expected):
        assert bubble_sort(l_reversed) == l_expected
        
    def test_selection(self, l_reversed, l_expected):
        assert selection_sort(l_reversed) == l_expected
        
    def test_quick(self, l_reversed, l_expected):
        assert quicksort(l_reversed) == l_expected

@pytest.fixture()
def l_random():
    l = [x for x in range(20)]
    random.seed(1337)
    return random.sample(l, len(l))

class Test_random_list(object):
    def test_insertion(self, l_random, l_expected):
        assert insertion_sort(l_random) == l_expected
        
    def test_bubble(self, l_random, l_expected):
        assert bubble_sort(l_random) == l_expected
        
    def test_selection(self, l_random, l_expected):
        assert selection_sort(l_random) == l_expected
        
    def test_quick(self, l_random, l_expected):
        assert quicksort(l_random) == l_expected
