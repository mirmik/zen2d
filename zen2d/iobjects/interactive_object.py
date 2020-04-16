import zen2d.trans

class interactive_object:
	def __init__(self):
		self.location = zen2d.trans.nulltrans()

	def draw(self, painter):
		raise NotImplementedError()

	def relocate(self, trsf):
		self.location = trsf