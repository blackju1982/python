#!/usr/local/bin/python3.5

#I honor Parkland's core values by affirming that I have 
#followed all academic integrity guidelines for this work.

#Justin Blackford

def circle():
    print('<circle cx="900" cy="50" r="40" fill="rgb(0,0,153)" />')

def rectangle():
	print('<rect width="300" height="100" style="fill:rgb(0,0,0);stroke-width:5;stroke:rgb(0,0,153)" />')

def namesvg():
	print('<text x="100" y="50" fill="red">Justin Blackford</text>')

print("Content-type: text/html\n\n")
print("<html><head></head><body>")
print('<svg height="1000" width="1000">')

# call a function that prints the circle 
circle()
# call a function that prints the rectangle 
rectangle()
# call a function that prints your name in the rectangle
namesvg()

print('</svg>')
print("</body></html>")
