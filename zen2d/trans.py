from zen2d.pntvec import vector

class transformation:
	def __init__(self, ang, lin):
		self.ang = ang
		self.lin = vector(lin)

	def transform(self, obj):
		return obj.transformed_by(self)

	def __call__(self, obj):
		return self.transform(obj)

	def __mul__(self, oth):
		ang = self.ang + oth.ang
		lin = self.lin + self(oth.lin)

		return transformation(ang, lin)

def rotate(ang):
	return transformation(ang, (0,0))

def translate(x, y=None):
	if y is None:
		x, y = x
	return transformation(0, (x,y))

def nulltrans():
	return transformation(0, (0,0))