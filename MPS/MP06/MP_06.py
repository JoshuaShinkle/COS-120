import time
"""
Starting with the 8x8 board solution that will be appended here
after MP05 is due, add the following functionality:
1) Add code to create a list, containing 8 lists, with each of the 8 lists
containing 8 null strings as values.  Call the list of lists board.
2) Now write code that will visit each valid playing square of the graphical
board for the first three rows (A,B and C) and place red checkers in each of
the valid playing squares.  Be sure to modify the list of lists so that each
of the logical locations in board now reflects if a red checker is contained
there ("r" instead of "").  Do the same with the last 3 rows ((F,G,H), but
place black checkers on the graphical board, with "b" instead of "" for black
checkers placed in logical board.
3) If you are wondering why I made you place these as separate operations
instead of hard-coding them when the board is first created, keep in mind in
the future we may want to read in one or both players' locations from a saved
game file or files instead of setting up a new game.  This allows playing from
an incomplete state, and REALLY simplifies testing of certain configurations
of checkers....
4) Write a simple main game loop that first asks one user (start with black)
from where they wish to move a checker and the location to move it to.  Do this
in the form A0:B1 (FROM:TO) where A0 is the FROM location and B1 is the TO
location.  Use a while loop that continues this process, alternating players,
until they type "quit" instead of a valid move.  If they enter an invalid move,
e.g. "A0:B0 or A1:B1",  OR a FROM location that contains an opposing checker color
or is empty, OR a TO location that already contains a checker, disallow the move
and ask for another move (do this until they either enter quit or give you a good
move).  YOU DO NOT HAVE TO ENFORCE ANY OF THE OTHER RULES OF CHECKERS YET!  Checkers
can move anywhere on the playing board where there is an empty space, as long as in
the FROM location is a checker of the color whose turn it is, and the TO location
is a valid empty square. Jumps do not really exist, etc.  You may not move opposing
checkers, and you may move in any diagonal direction on the board from a valid
starting square, etc.
(IF YOU FIND IT HELPFUL, YOU MAY PUT THE GAME INTO AN INFINITE LOOP AND GET RID OF
CHECKING FOR quit, at least at first)
"""

import turtle

def drawFilledSquare(t,sideLength,color):
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.forward(sideLength)
        t.left(90)
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
    t1.left(90)
    t1.forward(sz)
    t1.right(90)
    t1.down()

def drawChecker(t,wn,row,col,color,ringColor,board):
    wn.tracer(False)
    t.color("black",color)
    t.begin_fill()
    t.up()
    t.goto(col+.5,row)
    t.down()
    t.circle(.48)
    t.end_fill()
    t.color(ringColor)
    for size in range(1,5):
        t.up()
        t.goto(col+.5,row+(.5-(size*.1)-.02))
        t.down()
        t.circle(size*.1)
    wn.tracer(True)


def drawLabel(t,wn,row,col):
    wn.tracer(False)
    t.up()
    t.color("white","white")
    t.goto(col+.81,row+1.03)
    t.write(chr(row+65)+str(col), font=("courier new",10,"bold"))
    wn.tracer(True)

def setupBoard(sz):
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,9,9.5,-1)
    t=turtle.Turtle()
    wn.tracer(False)
    for i in range(4):
        drawCheckerRow(t,sz,"red","gray")
        positionTurtlefForNextRow(t,sz)
        drawCheckerRow(t,sz,"gray","red")
        positionTurtlefForNextRow(t,sz)
    validSquaresList=[]
    for row in range(8):
        for col in range(8):
            if (row+col)%2==1:
                drawLabel(t,wn,row,col)
                validSquaresList.append(chr(row+65)+str(col))
    wn.tracer(True)
    t.hideturtle()
    row=[""]*8
    board=[]
    for i in range(8):
        board.append(row[:])
    return t,wn,validSquaresList,board

def newGame(t,wn,board):
    for row in range(0,3):
        for col in range(8):
            if (row+col)%2==1:
                board[row][col]="r"
                drawChecker(t,wn,row,col,"red","black",board)
    for row in range(5,8):
        for col in range(8):
            if (row+col)%2==1:
                board[row][col]="b"
                drawChecker(t,wn,row,col,"black","gray",board)

def showBoard(board):
    print("Board State")
    index=0
    print ("  01234567")
    for row in board:
        print(chr(index+65)+" ",end="")
        index+=1
        for col in row:
            if col=="":
                print("-",end="")
            else:
                print(col,end="")
        print()
    print()

def getValidMove(player,board,validSquaresList):
    selectedChecker = input("Enter location of the checker you want to move-> ")
    if selectedChecker.lower() == "quit":
        fromTo = "QUIT"
    else:
        moveLocation = input("Enter location of the square you want to move to-> ")
        if moveLocation.lower() == "quit":
            fromTo = "QUIT"
        else:
            fromTo = selectedChecker + ":" + moveLocation
    return fromTo

def switchPlayer(currentPlayer):
    if currentPlayer=="black":
        currentPlayer="red"
    else:
        currentPlayer="black"
    return currentPlayer

def removeChecker(t,wn,fromRow,fromCol,board,sz):
    board[fromRow][fromCol]=""
    t.up()
    t.goto(fromCol,fromRow)
    drawFilledSquare(t,sz,"gray")
    drawLabel(t,wn,fromRow,fromCol)
    
def checkers():
    sz=1
    t,wn,validSquaresList,board=setupBoard(sz)
    showBoard(board)
    newGame(t,wn,board)
    showBoard(board)
    currentPlayer="black"
    
    while(1):
        move=getValidMove(currentPlayer,board,validSquaresList)
        if currentPlayer == "black":
            letterPlayer = "b"
        else:
            letterPlayer = "r"
        #print(board[2][7])
        board[2][5] = "b"
        showBoard(board)
        if move !="QUIT":
            fromRow=ord(move[0])-65
            fromCol=int(move[1])
            toRow=ord(move[3])-65
            toCol=int(move[4])
            removeChecker(t,wn,fromRow,fromCol,board,sz)
            drawChecker(t,wn,toRow,toCol,currentPlayer,"gray",board)
            board[toRow][toCol]=currentPlayer[0]
            showBoard(board)
            currentPlayer=switchPlayer(currentPlayer)
        else:
            return


checkers()