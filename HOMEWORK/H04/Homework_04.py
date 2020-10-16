import turtle

#Exercise 6.13.6
def drawPoly(turtle,numSides,sideSize):
    for i in range(numSides):
        turtle.forward(sideSize)
        turtle.left(360/numSides)
        
def drawEquitriangle(turtle, sideSize):
    drawPoly(turtle,3,sideSize)

lance = turtle.Turtle()

drawEquitriangle(lance, 100)

#Exercise 6.13.7
def sumTo(n):
    collectiveSum = (n * (n + 1)) / 2
    return int(collectiveSum)

print("Sum of numbers:",sumTo(10))
