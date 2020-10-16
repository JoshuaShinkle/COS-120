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
    t.color("black",color)
    t.begin_fill()
    t.up()
    t.goto(col,row)
    t.down()
    t.circle(.5)
    t.end_fill()
    for size in range(1,5):
        t.up()
        t.goto(col,row+(.5-(size*.1)))
        t.down()
        t.circle(size*.1)

def drawLabels(turtle):
    rows = ["A","B","C","D","E","F","G","H"]
    cols = [0,1,2,3,4,5,6,7,8]
    for i in rows:
        for j in cols:
            turtle.up()
            row = int(ord(i) - 65)
            col = j
            turtle.goto(col-0.25,row+0.25)
            turtle.down()
            if col % 2 != 0 and row % 2 != 0:
                style = ('Courier', 30, 'italic')
                turtle.write(str(i) + str(j), font = style)
            elif col % 2 == 0 and row % 2 == 0:
                style = ('Courier', 30, 'italic')
                turtle.write(str(i) + str(j), font = style)
        
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
    joe.color("white")
    drawLabels(joe)
    last = [0,0]
    while(1):
        position = input("Where do you want to place the checker? ")
        if position == "quit":
            break
        row = int(ord(position[0]) - 65)
        col = int(position[1])
        if col % 2 != 0 and row % 2 != 0:
            drawChecker(joe,last[0],last[1],"black")
            joe.color("white")
            drawLabels(joe)
            drawChecker(joe,row,col,"green")
            last[0] = row
            last[1] = col
        elif col % 2 == 0 and row % 2 == 0:
            drawChecker(joe,last[0],last[1],"black")
            joe.color("white")
            drawLabels(joe)
            drawChecker(joe,row,col,"green")
            last[0] = row
            last[1] = col

checkers(1)
