#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have
#followed all academic integrity guidelines for this work.

#Justin Blackford

from point import Point
from color import Color

class Circle(object):
	def __init__(self, center , radius, fill):
		self._center = center
		self._radius = radius
		self._fill = fill

	def setRadius(self, r):
		self._radius = r

	def getRadius(self):
		return self._radius

	def SVG(self):
        	return print("<circle cx=" + str(self._center.getAcross()) + " cy=" + str(self._center.getDown()) + " r=" + 
str(self.getRadius()) + " style='fill:" + str(self._fill.SVG()) + "' />")

#Testing
if __name__ == "__main__":
	tempPoint = Point(500, 500)
	tempColor = Color(0, 0, 153)

	newCircle = Circle(tempPoint, 40, tempColor)
	newCircle.SVG()

	print(newCircle.getRadius())
	newCircle.setRadius(50)
	print(newCircle.getRadius())
	newCircle.SVG()


	print(newCircle._center.getAcross())
	print(newCircle._center.getDown())
	newCircle._center.setAcross(400)
	newCircle._center.setDown(400)
	newCircle.SVG()
