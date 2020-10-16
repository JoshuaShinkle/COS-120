import turtle

#Exercise 6.13.3
def drawPoly(turtle,numSides,sideSize):
    for i in range(numSides):
        turtle.forward(sideSize)
        turtle.left(360/numSides)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)

drawPoly(tess,8,50)

#Exercise 6.13.4
def drawSquare(turtle,size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.left(18)

wn.reset()
tess.color("blue")
tess.pensize(2)

for x in range(20):
    drawSquare(tess,50)

#Exercise 6.13.5
def drawSpiral(angle):
    for i in range(0,199,2):
        tess.forward(i)
        tess.right(angle)

wn.reset()
tess.color("blue")
tess.pensize(2)

tess.up()
tess.goto(-200,0)
tess.down()

drawSpiral(90)
    
tess.up()
tess.goto(200,0)
tess.down()

drawSpiral(89)
