from abc import ABC, abstractmethod


class AlgoMixin(ABC):
    def __init__(self):
        self.get_data = dict()
        self.predict_data = dict()
        self.score_data = None

    @abstractmethod
    def get(self):
        # Should append to self.get_data and return nothing
        pass

    @abstractmethod
    def predict(self):
        # Should append to self.predict_data and return nothing
        pass

    @abstractmethod
    def score(self):
        # Should append to self.score_data and return nothing
        pass

    def run(self):
        self.get()
        self.predict()
        self.score()
        return