from algo_mixin import AlgoMixin
from get import GetMixin, GetB, GetC
from model import ModelMixin, Model2, Model3

class Algo2(
    GetMixin,
    GetB,
    GetC,
    ModelMixin,
    Model2,
    Model3,
    AlgoMixin,
):
    def __init__(self):
        super().__init__()

    def score(self):
        self.score_data = self.predict_data['model2'] + self.predict_data['model3'] + 3
