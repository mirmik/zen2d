from zen2d.iobjects.interactive_object import interactive_object
from zen2d.pntvec import point

class line(interactive_object):
	def __init__(self, pnt0, pnt1):
		super().__init__()
		self.pnt0 = point(pnt0)
		self.pnt1 = point(pnt1)

	def draw(self, painter):
		print(self.pnt0, self.pnt1)
		painter.draw_line(self.location(self.pnt0), self.location(self.pnt1))