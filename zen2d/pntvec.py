import math

class xy:
	def __init__(self, x, y=None):
		if y is None:
			self.x = x[0]
			self.y = x[1]
			return

		self.x = x
		self.y = y

	def __str__(self):
		return f"({self.x},{self.y})"

class point(xy):
	def transformed_by(self, trans):
		ang = trans.ang
		lin = trans.lin

		x = math.cos(ang) * self.x - math.sin(ang) * self.y + lin.x 
		y = math.sin(ang) * self.x + math.cos(ang) * self.y + lin.y

		return point(x,y)

	def __sub__(self, oth):
		return vector(self.x-oth.x, self.y-oth.y)

class vector(xy):
	def transformed_by(self, trans):
		ang = trans.ang
		lin = trans.lin

		x = math.cos(ang) * self.x - math.sin(ang) * self.y 
		y = math.sin(ang) * self.x + math.cos(ang) * self.y

		return point(x,y)

	def __mul__(self, oth):
		return vector(self.x*oth, self.y*oth)