from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from zen2d.pntvec import point, vector

class painter:
	def __init__(self, view):
		self.qpainter= QPainter(view)
		self.view = view

	def draw_line(self, pnt0, pnt1):
		self.qpainter.drawLine(self.proj(pnt0), self.proj(pnt1))

	def proj(self, pnt):
		w = self.view.width()
		h = self.view.height()

		locpnt = (pnt - self.view.center) * self.view.scale

		return QPoint(w/2 + locpnt.x, h/2 - locpnt.y) 

class view(QWidget):
	def __init__(self, scn):
		super().__init__()
		self.scn = scn
		self.center = point(0,0)
		self.scale = 1
		
	def set_scene(self, scn):
		self.scn = scn

	def redraw(self):
		p = painter(self)
		for i in self.scn.iobjs:
			i.draw(p)

	def paintEvent(self, ev):
		self.redraw()