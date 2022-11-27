import pytest
from algo2 import Algo2


class TestAlgo2(object):
    def test_initialize(self):
        a = Algo2()
        assert a.get_data == dict()
        assert a.model_data == dict()
        assert a.score_data == None

    def test_get(self):
        a = Algo2()
        a.get()
        assert a.get_data == {'b': 10, 'c': 100}

    def test_predict(self):
        a = Algo2()
        a.get()
        a.model()
        assert a.model_data == {'model2': 20, 'model3_pre': 9, 'model3': 100, 'model3_post': 300}

    def test_score(self):
        a = Algo2()
        a.get()
        a.model()
        a.score()
        assert a.score_data == 323

    def test_run(self):
        a = Algo2()
        a.run()
        assert a.get_data == {'b': 10, 'c': 100}
        assert a.model_data == {'model2': 20, 'model3_pre': 9, 'model3': 100, 'model3_post': 300}
        assert a.score_data == 323
