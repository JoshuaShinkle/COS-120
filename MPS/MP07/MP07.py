"""
MP07:
Starting with the MP06 solution appended below, add the following functionality:

0) Write a function called getValidMovesList that given the logical board and the current
player and a legal row increment for that player (1 or -1), returns a list of simple valid
moves that player can make (in the form ["A0:B1","A2:B1", . . . ]).  The list contains
simple moves (no jumps).
1) Write a function called getValidSingleJumpsList that given the logical board and the
current player and a legal row increment for that player (1 or -1),  returns a list of s
ingle jumps that player can make (in the form ["A0:C2", etc])
2) Modify the function getValidMove (rename it getValidPlayerAction) to take the board
and current player as parameters, and to generate the  validMoves list and the singleJumps
list described above, and not return to the main until a valid action (a jump, or a move if
no jumps are available) has been entered.  Valid moves for this version of the manual game
will be simply determined as a) if there are any jumps, one of them must be taken (standard
checker rules), and b) if there are no jumps, a legal simple move must be taken.  If the user
specifies something other than an available jump, print a message to that effect and keep
asking until they select an available jump.  If there are no jumps, the user may enter any of
the available moves found in the valid moves list.  In every case, an ill-formed jump or move
should result in a message and repeated entry of a move until a valid one is entered by the user
Make use of your listValidMoves and listSingleJumps functions to make the coding of your
getValidMove much simpler!  THE JUMPS DO NOT HAVE TO ACTUALLY REMOVE THE JUMPED CHECKER YET!!!!
YOU MAY (BUT ARE NOT REQUIRED) WORK IN PAIRS ON THIS PROBLEM!  DO NOT FORGET TO RENAME STARTER
CODE TO MP07.py
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
                drawChecker(t,wn,row,col,"red","gray",board)
    for row in range(5,8):
        for col in range(8):
            if (row+col)%2==1:
                board[row][col]="b"
                drawChecker(t,wn,row,col,"black","gray",board)

def showLogicalBoard(board):
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

def switchPlayer(currentPlayer):
    if currentPlayer=="black":
        currentPlayer="red"
        rowInc=1
    else:
        currentPlayer="black"
        rowInc=-1
    return currentPlayer,rowInc

def removeChecker(t,wn,fromRow,fromCol,board,sz):
    wn.tracer(False)
    board[fromRow][fromCol]=""
    t.up()
    t.goto(fromCol,fromRow)
    drawFilledSquare(t,sz,"gray")
    t.color("white")
    drawLabel(t,wn,fromRow,fromCol)
    wn.tracer(True)

def parseValidMove(move):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    return fromRow,fromCol,toRow,toCol

def getValidMovesList(player,board,rowInc):
    validMovesList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col]==player[0]:
                for colInc in [1,-1]:
                    if row+rowInc<=7 and row+rowInc>=0 and \
                           col+colInc<=7 and col+colInc>=0 and \
                           board[row+rowInc][col+colInc]=="":
                        validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
    return validMovesList

def getValidSingleJumpsList(player, board, rowInc):
    validSingleJumpsList = []
    if player[0] == "b":
        jumpRowInc = -2
        oppPlayer = "r"
    else:
        jumpRowInc = 2
        oppPlayer = "b"
    
    for row in range(8):
        for col in range(8):
            if board[row][col]==player[0]:
                for jumpColInc in [2,-2]:
                    if jumpColInc == 2:
                        colInc = 1
                    else:
                        colInc = -1
                    if row+jumpRowInc<=7 and row+jumpRowInc>=0 and col+jumpColInc<=7 and col+jumpColInc>=0 and board[row+jumpRowInc][col+jumpColInc]=="" and board[row+rowInc][col+colInc]== oppPlayer:
                           validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+jumpRowInc+65)+str(col+jumpColInc))
    return validSingleJumpsList

def getValidPlayerAction(player,board,validSquaresList,rowInc):
    validMovesList=getValidMovesList(player,board,rowInc)
    validSingleJumpsList = getValidSingleJumpsList(player, board, rowInc)

    move=input("Enter move (e.g. A0:B1) for "+player+" => ").upper()
    
    if len(validSingleJumpsList) > 0:
        while move.upper() != "QUIT" and move.upper() not in validSingleJumpsList:
            print("Bad move! Make a valid jump! . . . try again!")
            move=input("Enter move (e.g. A0:B1) for "+player+" => ").upper()
        print()
        return move.upper()

    while move.upper() != "QUIT" and move.upper() not in validMovesList:
        print("Bad move . . .  try again!")
        move=input("Enter move (e.g. A0:B1) for "+player+" => ")
    print()
    return move.upper()
              
def checkers():
    sz=1
    t,wn,validSquaresList,board=setupBoard(sz)
    newGame(t,wn,board)
    currentPlayer="black"
    rowInc=-1
    move=getValidPlayerAction(currentPlayer,board,validSquaresList,rowInc)
    while move != "QUIT":
        fromRow,fromCol,toRow,toCol=parseValidMove(move)
        removeChecker(t,wn,fromRow,fromCol,board,sz)
        drawChecker(t,wn,toRow,toCol,currentPlayer,"gray",board)
        board[toRow][toCol]=currentPlayer[0]
        currentPlayer,rowInc=switchPlayer(currentPlayer)
        move=getValidPlayerAction(currentPlayer,board,validSquaresList,rowInc)

checkers()
