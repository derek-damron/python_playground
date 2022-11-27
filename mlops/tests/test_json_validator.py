import pytest
from get import GetBase

class TestGet(object):
    class GetD(GetBase):
        @property
        def source(self):
            return 'https://www.data.com/d'

        def get(self):
            self.get_data['d'] = {'d1': 'dd', 'd2': 20}
            super().get()

    def test_getd(self):
        a = Algo2()