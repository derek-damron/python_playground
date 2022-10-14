from algo_mixin import AlgoMixin
from score_mixin import ScoreMixin
from get_mixin import GetMixin, GetB, GetC

class Algo2(
    GetMixin,
    GetB,
    GetC,
    ScoreMixin,
    AlgoMixin,
):
    def __init__(self):
        super().__init__()

    # Modify "default" scoring function
    def score(self):
        super().score()
        self.score_data *= 2
        return
