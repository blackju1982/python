#!usr/bin/local/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

#!usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.

#Justin Blackford

class Point(object):
	def __init__(self, _across, _down):
		self._across = _across
		self._down = _down

	def setAcross(self, x):
		self._across = x

	def setDown(self, y):
		self._down = y

	def getAcross(self):
		return self._across

	def getDown(self):
		return self._down

#Testing
if __name__ == "__main__":
	point = Point(10, 5)
	print(point.getDown())
	print(point.getAcross())
	point.setAcross(5)
	point.setDown(10)
	print(point.getDown())
	print(point.getAcross())
