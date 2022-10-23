from abc import ABC, abstractmethod


class ModelBase(ABC):
    @property
    @abstractmethod
    def source(self):
        pass

    @abstractmethod
    def model(self):
        # Should append to self.model_data and return nothing
        pass


class Model1(ModelBase): 
    def source(self):
        return 'https://www.model.com/1'

    def model(self):
        self.model_data['model1'] = self.get_data['a'] + 2 * self.get_data['b']
        super().model()


class Model2(ModelBase):
    def source(self):
        return 'https://www.model.com/2'

    def model(self):
        self.model_data['model2'] = 2 * self.get_data['b']
        super().model()


class Model3(ModelBase):
    def source(self):
        return 'https://www.model.com/3'

    def model(self):
        self._pre_model()
        self._model()
        self._post_model()
        super().model()

    @staticmethod
    def z_score(x):
        return (x - 10) / 10

    @staticmethod
    def z_score_inverse(x):
        return 10 * x + 10

    def _pre_model(self):
        self.model_data['model3_pre'] = self.z_score(self.get_data['c'])

    def _model(self):
        self.model_data['model3'] = self.z_score_inverse(self.model_data['model3_pre'])

    def _post_model(self):
        self.model_data['model3_post'] = self.model_data['model3'] * 3
