import turtle

#Exercise 6.13.1
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

lance = turtle.Turtle()
lance.color("hotpink")
lance.pensize(3)

for x in range(5):
    drawSquare(lance, 20)
    lance.up()
    lance.forward(40)
    lance.down()

#Exercise 6.13.1
wn.clearscreen()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

lance = turtle.Turtle()
lance.color("hotpink")
lance.pensize(3)

squareSize = 0

for x in range(5):
    squareSize = squareSize + 20
    drawSquare(lance, squareSize)
    lance.up()
    lance.back(10)
    lance.right(90)
    lance.forward(10)
    lance.left(90)
    lance.down()
