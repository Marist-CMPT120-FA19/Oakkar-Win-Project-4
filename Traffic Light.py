Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> def main():
	#Window Name
	win=GraphWin("Traffic Light")
	#Horizontal Shape Traffic Light
	shape = Rectangle(Point(8,8),Point(90,120))
	shape . setOutline ("Black")
	shape . setFill ("White")
	#Red Circle
	shape.draw(win)
	shape=Circle(Point(50,100),15)
	shape.setOutline("Black")
	shape.setFill("Red")
	shape.draw(win)
	#Yellow Circle
	shape=Circle(Point(50,65),15)
	shape.setOutline("Black")
	shape.setFill("Yellow")
	shape.draw(win)
	#Green Circle
	shape=Circle(Point(50,30),15)
	shape.setOutline("Black")
	shape.setFill("Green")
	shape.draw(win)
	input("Press <Enter> to quit")

	
>>> main ()
