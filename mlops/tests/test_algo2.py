import pytest
from algo2 import Algo2

class TestAlgo2(object):
    def test_get_data_empty(self):
        a = Algo2()
        assert a.get_data == dict()

    def test_get_data_populated(self):
        a = Algo2()
        a.get()
        assert a.get_data == {'b': 10, 'c': 100}

    def test_score(self):
        a = Algo2()
        a.get()
        assert a.score() == 220