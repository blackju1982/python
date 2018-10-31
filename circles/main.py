#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have
#followed all academic integrity guidelines for this work.

#Justin Blackford

from point import Point
from color import Color
from circle import Circle
from random import randint

print("Content-type: text/html\n\n")
print("<html><head></head><body>")
print('<svg height="1000" width="1000">')

circleList = []
i = 1
j = 0

firstPoint = Point(500, 500)
myColor = Color(0, 0 , 153)

firstCircle = Circle(firstPoint, 40, myColor)
circleList.append(firstCircle)

while i < 100:
	x = randint(0, 1000)
	y = randint(0, 1000)
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)

	tempPoint = Point(x, y)
	tempColor = Color(r, g, b)
	
	tempCircle = Circle(tempPoint, 40, tempColor)
	circleList.append(str(tempCircle.SVG()))
	i += 1

while j < len(circleList):
        circleList[j].SVG()
        j += 1

print('</svg>')
print("</body></html>")
