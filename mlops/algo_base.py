from abc import ABC, abstractmethod


class AlgoBase(ABC):
    def __init__(self):
        self.get_data = dict()
        self.model_data = dict()
        self.score_data = None

    @abstractmethod
    def get(self):
        # Should append to self.get_data and return nothing
        pass

    @abstractmethod
    def model(self):
        # Should append to self.model_data and return nothing
        pass

    @abstractmethod
    def score(self):
        # Should append to self.score_data and return nothing
        pass

    def run(self):
        self.get()
        self.model()
        self.score()
        return