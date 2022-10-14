class ModelMixin(object):
    def predict(self):
        super().predict()


class Model1(object):
    def predict(self):
        self.predict_data['model1'] = self.get_data['a'] + 2 * self.get_data['b']
        super().predict()


class Model2(object):
    def predict(self):
        self.predict_data['model2'] = 2 * self.get_data['b']
        super().predict()


class Model3(object):
    def predict(self):
        self.predict_data['model3'] = 3 * self.get_data['c']
        super().predict()
