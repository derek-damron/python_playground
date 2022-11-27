from algo_base import AlgoBase
from get import GetB, GetC
from model import Model2, Model3

class Algo2(
    GetB,
    GetC,
    Model2,
    Model3,
    AlgoBase,
):
    def __init__(self):
        super().__init__()

    def score(self):
        self.score_data = self.model_data['model2'] + self.model_data['model3_post'] + 3
