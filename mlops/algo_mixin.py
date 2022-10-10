from abc import ABC, abstractmethod

class AlgoMixin(ABC):
    def __init__(self):
        self.get_data = dict()

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def score(self):
        pass
