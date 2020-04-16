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

		self.zoom_koeff_mouse = 1.1
		
	def set_scene(self, scn):
		self.scn = scn

	def redraw(self):
		p = painter(self)
		for i in self.scn.iobjs:
			i.draw(p)

	def paintEvent(self, ev):
		self.redraw()


	def onMouseWheel(self, theFlags, theDelta, thePoint):
		if theDelta.y() > 0:
			self.scale *= self.zoom_koeff_mouse
		else:
			self.scale /= self.zoom_koeff_mouse

	def onMouseMove(self, theFlags, thePoint):
		diff = self.temporary1 - thePoint

		if theFlags & Qt.LeftButton or self.alt_pressed:
			self.center = self.center + vector(diff.x(), -diff.y()) / self.scale

		self.temporary1 = thePoint

	def wheelEvent(self, e):
		self.onMouseWheel(e.buttons(), e.angleDelta(), e.pos())
		self.update()

	def mouseMoveEvent(self, e):
		self.onMouseMove(e.buttons(), e.pos())
		self.update()



	def onLButtonDown(self, theFlags, thePoint):
		self.temporary1 = thePoint

	def onRButtonDown(self, theFlags, thePoint):
		self.temporary1 = thePoint

	def onMButtonDown(self, theFlags, thePoint):
		self.temporary1 = thePoint


	def mouseReleaseEvent(self, e):
		self.mousedown = False

	def mousePressEvent(self, e):
		self.mousedown = True
		if e.button() == Qt.LeftButton:
			self.onLButtonDown((e.buttons() | e.modifiers()), e.pos())

		elif e.button() == Qt.MidButton:
			self.onMButtonDown((e.buttons() | e.modifiers()), e.pos())

		elif e.button() == Qt.RightButton:
			self.onRButtonDown((e.buttons() | e.modifiers()), e.pos())