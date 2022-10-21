from abc import ABC, abstractmethod


class ModelBase(ABC):
    @property
    @abstractmethod
    def source(self):
        pass

    @abstractmethod
    def predict(self):
        # Should append to self.predict_data and return nothing
        pass


class Model1(ModelBase):
    def source(self):
        return 'https://www.model.com/1'

    def predict(self):
        self.predict_data['model1'] = self.get_data['a'] + 2 * self.get_data['b']
        super().predict()


class Model2(ModelBase):
    def source(self):
        return 'https://www.model.com/2'

    def predict(self):
        self.predict_data['model2'] = 2 * self.get_data['b']
        super().predict()


class Model3(ModelBase):
    def source(self):
        return 'https://www.model.com/3'

    def predict(self):
        self._pre_predict()
        self._predict()
        self._post_predict()
        super().predict()

    @staticmethod
    def z_score(x):
        return (x - 10) / 10

    @staticmethod
    def z_score_inverse(x):
        return 10 * x + 10

    def _pre_predict(self):
        self.predict_data['model3_pre'] = self.z_score(self.get_data['c'])

    def _predict(self):
        self.predict_data['model3'] = self.z_score_inverse(self.predict_data['model3_pre'])

    def _post_predict(self):
        self.predict_data['model3_post'] = self.predict_data['model3'] * 3
