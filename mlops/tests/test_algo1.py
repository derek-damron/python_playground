import pytest
from algo1 import Algo1

class TestAlgo1(object):
    def test_initialize(self):
        a = Algo1()
        assert a.get_data == dict()
        assert a.predict_data == dict()
        assert a.score_data == None

    def test_get(self):
        a = Algo1()
        a.get()
        assert a.get_data == {'a': 1, 'b': 10}

    def test_predict(self):
        a = Algo1()
        a.get()
        a.predict()
        assert a.predict_data == {'model1': 21}

    def test_score(self):
        a = Algo1()
        a.get()
        a.predict()
        a.score()
        assert a.score_data == 23

    def test_run(self):
        a = Algo1()
        a.run()
        assert a.get_data == {'a': 1, 'b': 10}
        assert a.predict_data == {'model1': 21}
        assert a.score_data == 23
