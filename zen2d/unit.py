from zen2d.iobjects.interactive_object import interactive_object
from zen2d.trans import nulltrans

class unit(interactive_object):
	def __init__(self):
		super().__init__()
		self.parent = None
		self.childs = []
		self.views = []
		self.location = nulltrans()

	def relocate(self, trsf, deep=True):
		self.location = trsf
		self.location_update(deep)

	def add(self, iobj):
		self.views.append(iobj)

	def location_update(self, deep=True):
		if self.parent is None:
			self.global_location = self.location
		else:
			self.global_location = parent.global_location * self.location
			
		if deep:
			for c in self.childs:
				c.location_update(deep=True)

		for i in self.views:
			i.relocate(self.global_location)


	def draw(self, painter):
		for c in self.views:
			c.draw(painter)