from zen2d.pntvec import vector

class transformation:
	def __init__(self, ang, lin):
		self.ang = ang
		self.lin = vector(lin)

	def transform(self, obj):
		return obj.transformed_by(self)

	def __call__(self, obj):
		return self.transform(obj)

def rotate(ang):
	return transformation(ang, (0,0))

def translate(lin):
	return transformation(ang, lin)

def nulltrans():
	return transformation(0, (0,0))