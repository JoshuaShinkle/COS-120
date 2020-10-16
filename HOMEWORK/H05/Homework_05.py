import math
import turtle

#Exercise 6.13.8
def areaOfCircle(r):
    area = math.pi * (r**2)
    return area

print("Area =",areaOfCircle(5))

#Exercise 6.13.9
def drawStar(sideSize):
    for x in range(5):
        lance.forward(sideSize)
        lance.right(144)
    
lance = turtle.Turtle()

drawStar(100)

#Exercise 6.13.10
wn = turtle.Screen()
wn.reset()
wn.bgcolor("lightgreen")

lance.pensize(3)
lance.color("hotpink")

lance.up()
lance.goto(-200,0)
lance.down()

for i in range(5):
    drawStar(100)
    lance.up()
    lance.forward(350)
    lance.right(144)
    lance.down()
