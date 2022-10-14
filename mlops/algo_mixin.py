from abc import ABC, abstractmethod

class AlgoMixin(ABC):
    def __init__(self):
        self.get_data = dict()

    @abstractmethod
    def get(self):
        # Should append to self.get_data and return nothing
        pass

    @abstractmethod
    def score(self):
        # Should append to self.score_data and return nothing
        pass

    def run(self):
        self.get()
        self.score()
        return