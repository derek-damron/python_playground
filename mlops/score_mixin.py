class ScoreMixin(object):
    def score(self):
        s = 0
        for k, v in self.get_data.items():
            s += v
        return s
