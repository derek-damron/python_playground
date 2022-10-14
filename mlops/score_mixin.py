class ScoreMixin(object):
    def score(self):
        s = 0
        for k, v in self.get_data.items():
            s += v
        self.score_data = s
        return
