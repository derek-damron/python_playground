from abc import ABC, abstractmethod


class GetBase(ABC):
    @property
    @abstractmethod
    def source(self):
        pass

    @abstractmethod
    def get(self):
        # Should append to self.get_data and return nothing
        pass


class GetA(GetBase):
    @property
    def source(self):
        return 'https://www.data.com/a'

    def get(self):
        self.get_data['a'] = 1
        super().get()


class GetB(GetBase):
    @property
    def source(self):
        return 'https://www.data.com/b'

    def get(self):
        self.get_data['b'] = 10
        super().get()


class GetC(GetBase):
    @property
    def source(self):
        return 'https://www.data.com/c'

    def get(self):
        self.get_data['c'] = 100
        super().get()
