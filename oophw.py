class Line:

	def __init__(self, coor1, coor2):
		(self.x1, self.y1) = coor1
		(self.x2, self.y2) = coor2
		#tuple unpacking
		# x1,y1 = self.coor1
		# x2,y2 = self.coor2
		# self.x1 = coor1[1]
	def distance(self):
		distance = ((self.x2-self.x1)**2 + (self.y2 -self.y1)**2 )**0.5
		return distance

	def slope(self):
		slope = (self.y2 - self.y1)/(self.x2-self.x1)
		return slope


class Cylinder:
	pie =3.14
	def __init__(self, height=1, radius=1):
		self.h = height
		self.r = radius

	def volume(self):

		v = self.pie * (self.r**2) * self.h
		return v
	def area(self):

		a = ((2*self.pie)*self.r*self.h) + ((2*self.pie)*(self.r**2))
		return a

line = Line((3,2),(8,10))
cylin = Cylinder()
print(line.distance())


print(line.slope())

print(cylin.area())
print(cylin.volume())



