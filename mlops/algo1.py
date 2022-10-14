from algo_mixin import AlgoMixin
from get import GetMixin, GetA, GetB
from model import ModelMixin, Model1

class Algo1(
    GetMixin,
    GetA,
    GetB,
    ModelMixin,
    Model1,
    AlgoMixin
):
    def __init__(self):
        super().__init__()

    def score(self):
        self.score_data = self.predict_data['model1'] + 2