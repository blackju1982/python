#!usr/bin/local/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.
#Justin Blackford

#!usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.

#Justin Blackford

class Color(object):
	def __init__(self, red, green, blue):
		self._red = red
		self._green = green
		self._blue = blue

	def setRed(self, red):
		self._red = red

	def setGreen(self, green):
		self._green = green

	def setBlue(self, blue):
		self._blue = blue

	def getRed(self):
		return self._red

	def getGreen(self):
		return self._green

	def getBlue(self):
		return self._blue
	
	def SVG(self):
		return "rgb(" + str(self.getRed()) + ", " + str(self.getGreen()) + ", " + str(self.getBlue()) + ")"

#testing
if __name__ == "__main__":

	color = Color(0, 255, 125)
	print(color.getRed())
	print(color.getGreen())
	print(color.getBlue())
	color.setRed(125)
	color.setGreen(0)
	color.setBlue(255)
	print(color.getRed())
	print(color.getGreen())
	print(color.getBlue())
	print(color.SVG())
