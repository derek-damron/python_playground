import pytest
from algo1 import Algo1

class TestAlgo1(object):
    def test_get_data_empty(self):
        a = Algo1()
        assert a.get_data == dict()

    def test_get_data_populated(self):
        a = Algo1()
        a.get()
        assert a.get_data == {'a': 1, 'b': 10}

    def test_score(self):
        a = Algo1()
        a.get()
        a.score()
        assert a.score_data == 11

    def test_run(self):
        a = Algo1()
        a.run()
        assert a.get_data == {'a': 1, 'b': 10}
        assert a.score_data == 11
