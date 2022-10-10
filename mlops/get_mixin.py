class GetMixin(object):
	def get(self):
		super().get()


class GetA(object):
	def get(self):
		self.get_data['a'] = 1
		super().get()


class GetB(object):
	def get(self):
		self.get_data['b'] = 10
		super().get()


class GetC(object):
	def get(self):
		self.get_data['c'] = 100
		super().get()
