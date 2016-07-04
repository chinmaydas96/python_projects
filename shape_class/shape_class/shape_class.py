import math


class shape(object):
	def Area(self):
		pass
	def perimeter(self):
		pass	


class square(shape):
	def __init__(self,side_length):
		self.side=side_length
	def Area(self):
		return	self.side * self.side	
	def perimeter(self):
		return 4* self.side

class rectangle(shape):
	def __init__(self,length,width):
		self.length=length`	
		self.width=width
	def Area(self):
		return self.length*self.width
	def perimeter(self):
		return 2 * self.length + 2 * self.width

class circle(shape):
	def __init__(self,radius):
		self.radius=radius
	def Area(self):
		return math.pi * self.radius * self.radius
	def perimeter(self):
		return 2 * math.pi * self.radius


class triangle(shape):
	"""
	Hi I am chinmay
	"""
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.s=(self.a+self.b+self.c)/2
	def validate(self):
		if (self.a + self.b  >self.c):
			pass
		elif(self.a + self.b >self.c):
			pass
		elif(self.a + self.b >self.c):
			pass
		else:
		     raise Exception("not valid triangle!")
		     
	
	def Area(self):
		s=self.s
		self.validate()
		return math.sqrt(s*(s-self.a) *(s-self.b) * (s-self.c))
	def perimeter(self):
		return self.a+self.b+self.c
