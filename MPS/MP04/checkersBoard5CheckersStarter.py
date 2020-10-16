"""
1) Add code to the drawChecker routine to make it work.
2) Add code to the main that 5 times asks the user for a row and a column and
then places a checker in that col and row location
"""
import turtle

def drawFilledSquare(t,sideLength,color):
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.forward(sideLength)
        t.right(90)
    t.end_fill()

def drawCheckerRow(tu,length,color1,color2):
    for ct in range(4):
        drawFilledSquare(tu,length,color1)
        tu.forward(length)
        drawFilledSquare(tu,length,color2)
        tu.forward(length)

def positionTurtlefForNextRow(t1,sz):
    t1.up()
    t1.backward(8*sz)
    t1.right(90)
    t1.forward(sz)
    t1.left(90)
    t1.down()

def drawChecker(t,row,col,color):
    t.goto(col-1, row-0.9)
    t.down()
    t.begin_fill()
    t.circle(0.4)
    t.end_fill()
    t.color("black")
    t.up()
    t.goto(col-1, row-0.8)
    t.down()
    t.circle(0.3)
    t.up()
    t.goto(col-1, row-0.7)
    t.down()
    t.circle(0.2)
    t.up()
    t.goto(col-1, row-0.6)
    t.down()
    t.circle(0.1)
    
def checkers(sz):
    wn=turtle.Screen()
    joe=turtle.Turtle()
    wn.setworldcoordinates(-1.5,-1.5,9.5,9) #bottom left of board is -1,-1, upper right is 9,9
    wn.tracer(False)
    joe.up()
    joe.goto(-.5,8)
    joe.down()
    joe.speed(0)
    for i in range(4):
        drawCheckerRow(joe,sz,"red","black")
        positionTurtlefForNextRow(joe,sz)
        drawCheckerRow(joe,sz,"black","red")
        positionTurtlefForNextRow(joe,sz)
    wn.tracer(True)
    joe.hideturtle()

def main():
    checkers(1)
    lance = turtle.Turtle()
    lance.speed(0)
    lance.hideturtle()
    for x in range(5):
        lance.up()
        lance.color("white")
        row = int(input("Enter a row -> "))
        column = int(input("Enter a column -> "))
        drawChecker(lance, row, column, "white")
        print()

main()