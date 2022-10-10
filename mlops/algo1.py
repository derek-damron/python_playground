from algo_mixin import AlgoMixin
from score_mixin import ScoreMixin
from get_mixin import GetMixin, GetA, GetB

class Algo1(
    GetMixin,
    GetA,
    GetB,
    ScoreMixin,
    AlgoMixin
):
    def __init__(self):
        super().__init__()
