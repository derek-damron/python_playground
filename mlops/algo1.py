from algo_base import AlgoBase
from get import GetA, GetB
from model import Model1

class Algo1(
    GetA,
    GetB,
    Model1,
    AlgoBase
):
    def __init__(self):
        super().__init__()

    def score(self):
        self.score_data = self.predict_data['model1'] + 2