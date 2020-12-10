"""
0) Add the logic for completing a jump (removal of jumped checker)

1) Write the code that will ask the user for a file name to save the
game when they enter "quit".  If they just hit enter, do not save the
game.  If they type in anything else, save the state of the game using
the same conventions you see in the attached test file.

2) Add the logic for when a checker reaches the opposing end row, the
checker becomes an upper case letter in the logical board, and the checker
now should include a gold star center to show it is a king checker.  You DO
NOT have to yet add logic for moving a king checker in any direction.

3) Replace the win function stub with actual winning logic.
"""
import random
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

def positionTurtlefForNextRow(t1):
    t1.up()
    t1.backward(8)
    t1.left(90)
    t1.forward(1)
    t1.right(90)
    t1.down()

def drawChecker(t,wn,row,col,color,ringColor,board,isKing):
    if (color=="black" and row==0) or (color=="red" and row==7) or isKing == True:
        board[row][col]=color[0].upper()
    else:
        board[row][col]=color[0]
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
    if board[row][col] in ["B","R"]:
        t.up()
        t.goto(col+.25,row+.58)
        t.down()
        t.setheading(0)
        t.color("yellow")
        t.begin_fill()
        for i in range(5):
            t.forward(.5)
            t.right(144)
        t.end_fill()
    wn.tracer(True)

def drawLabel(t,wn,row,col):
    wn.tracer(False)
    t.up()
    t.color("white","white")
    t.goto(col+.81,row+1.03)
    t.write(chr(row+65)+str(col), font=("courier new",10,"bold"))
    wn.tracer(True)

def setupBoard():
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,9,9.5,-1)
    t=turtle.Turtle()
    wn.tracer(False)
    for i in range(4):
        drawCheckerRow(t,1,"red","gray")
        positionTurtlefForNextRow(t)
        drawCheckerRow(t,1,"gray","red")
        positionTurtlefForNextRow(t)
    for row in range(8):
        for col in range(8):
            if (row+col)%2==1:
                drawLabel(t,wn,row,col)
    wn.tracer(True)
    t.hideturtle()
    row=[""]*8
    board=[]
    for i in range(8):
        board.append(row[:])
    return t,wn,board

def newGame(t,wn,board):
    for row in range(0,3):
        for col in range(8):
            if (row+col)%2==1:
                board[row][col]="r"
                isKing = False
                drawChecker(t,wn,row,col,"red","gray",board,isKing)
    for row in range(5,8):
        for col in range(8):
            if (row+col)%2==1:
                board[row][col]="b"
                isKing = False
                drawChecker(t,wn,row,col,"black","gray",board,isKing)
    if random.randint(0,1)==0:
        currentPlayer="black"
        opposingPlayer="red"
        forwardRowInc=-1
        currentPlayerTokens=['b','B']
        opposingPlayerTokens=['r','R']
    else:
        currentPlayer="red"
        opposingPlayer="black"
        forwardRowInc=1
        currentPlayerTokens=['r','R']
        opposingPlayerTokens=['b','B']
    return currentPlayer,opposingPlayer,currentPlayerTokens,opposingPlayerTokens,forwardRowInc
    

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

def getValidPlayerAction(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc):
    validMovesList=listValidMoves(board,currentPlayerTokens,forwardRowInc)
    print("Valid Moves List",validMovesList)
    validSingleJumpsList=listValidSingleJumps(board,currentPlayerTokens,forwardRowInc,opposingPlayerTokens)
    print("Valid Single Jumps List",validSingleJumpsList)
    if len(validSingleJumpsList)>0:
        move=input("Enter jump for player "+player+" => ").upper()
        while move != "QUIT" and move not in validSingleJumpsList:
            print("Must take a jump . . .  try again!")
            move=input("Enter jump for player "+player+" => ").upper()
    else:
        move=input("Enter move for player "+player+" => ").upper()
        while move != "QUIT" and move not in validMovesList:
            print("Bad move . . .  try again!")
            move=input("Enter move for player "+player+" => ").upper()
    return move

def switchPlayer(currentPlayer):
    if currentPlayer=="black":
        currentPlayer="red"
        opposingPlayer="black"
        forwardRowInc=1
        currentPlayerTokens=['r','R']
        opposingPlayerTokens=['b','B']
    else:
        currentPlayer="black"
        opposingPlayer="red"
        forwardRowInc=-1
        currentPlayerTokens=['b','B']
        opposingPlayerTokens=['r','R']
    return currentPlayer,currentPlayerTokens,opposingPlayer,opposingPlayerTokens,forwardRowInc

def removeChecker(t,wn,fromRow,fromCol,board):
    wn.tracer(False)
    if board[fromRow][fromCol] == 'B' or board[fromRow][fromCol] == 'R':
        isKing = True
    else:
        isKing = False
    board[fromRow][fromCol]=""
    t.up()
    t.goto(fromCol,fromRow)
    drawFilledSquare(t,1,"gray")
    t.color("white")
    drawLabel(t,wn,fromRow,fromCol)
    wn.tracer(True)
    return isKing

def parseValidMove(move):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    return fromRow,fromCol,toRow,toCol

#function to return a list of all valid moves for the current player
def listValidMoves(board,currentPlayerTokens,rowInc):
    validMovesList=[]
    if currentPlayerTokens == ['b','B']:
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'b':
                    for colInc in [1,-1]:
                        if row+rowInc>=0 and row+rowInc <=7 \
                        and col+colInc>=0 and col+colInc<=7 \
                        and board[row+rowInc][col+colInc]=="":
                            validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
                elif board[row][col] == 'B':
                    for rowInc in [1,-1]:
                        for colInc in [1,-1]:
                            if row+rowInc>=0 and row+rowInc <=7 \
                            and col+colInc>=0 and col+colInc<=7 \
                            and board[row+rowInc][col+colInc]=="":
                                validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
    else:
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'r':
                    for colInc in [1,-1]:
                        if row+rowInc>=0 and row+rowInc <=7 \
                        and col+colInc>=0 and col+colInc<=7 \
                        and board[row+rowInc][col+colInc]=="":
                            validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
                elif board[row][col] == 'R':
                    for rowInc in [1,-1]:
                        for colInc in [1,-1]:
                            if row+rowInc>=0 and row+rowInc <=7 \
                            and col+colInc>=0 and col+colInc<=7 \
                            and board[row+rowInc][col+colInc]=="":
                                validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
    return validMovesList

#function to return a list of all valid jumps for the current player
def listValidSingleJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens): #Not finished
    validSingleJumpsList=[]
    if currentPlayerTokens == ['b','B']:
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'b':
                    for colInc in [1,-1]:
                        if row+rowInc*2>=0 and row+rowInc*2<=7 and \
                        col+colInc*2>=0 and col+colInc*2<=7 and \
                        board[row+rowInc][col+colInc] in opposingPlayerTokens and \
                        board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                            validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+2*rowInc+65)+str(col+colInc*2))
                elif board[row][col] == 'B':
                    for rowInc in [1,-1]:
                        for colInc in [1,-1]:
                            if row+rowInc*2>=0 and row+rowInc*2<=7 and \
                            col+colInc*2>=0 and col+colInc*2<=7 and \
                            board[row+rowInc][col+colInc] in opposingPlayerTokens and \
                            board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                                validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+2*rowInc+65)+str(col+colInc*2))
    else:
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'r':
                    for colInc in [1,-1]:
                        if row+rowInc*2>=0 and row+rowInc*2<=7 and \
                        col+colInc*2>=0 and col+colInc*2<=7 and \
                        board[row+rowInc][col+colInc] in opposingPlayerTokens and \
                        board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                            validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+2*rowInc+65)+str(col+colInc*2))
                elif board[row][col] == 'R':
                    for rowInc in [1,-1]:
                        for colInc in [1,-1]:
                            if row+rowInc*2>=0 and row+rowInc*2<=7 and \
                            col+colInc*2>=0 and col+colInc*2<=7 and \
                            board[row+rowInc][col+colInc] in opposingPlayerTokens and \
                            board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                                validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+2*rowInc+65)+str(col+colInc*2))
    return validSingleJumpsList

def oldGame(t,wn,board,gameName):
    outFile=open(gameName,"r")
    currentPlayer=outFile.readline()[:-1]
    currentPlayer,currentPlayerTokens,opposingPlayer,opposingPlayerTokens,forwardRowInc=switchPlayer(currentPlayer)
    currentPlayer,currentPlayerTokens,opposingPlayer,opposingPlayerTokens,forwardRowInc=switchPlayer(currentPlayer)
    lstLines=outFile.readlines()
    for row in range(len(lstLines)):
        for col in range(len(lstLines[row])-1):
            if (row+col)%2==1 and lstLines[row][col] != 'e':
                if lstLines[row][col] in ["b","B"]:
                    color="black"
                else:
                    color="red"
                if lstLines[row][col] == 'B' or lstLines[row][col] == 'R':
                    isKing = True
                else:
                    isKing = False
                drawChecker(t,wn,row,col,color,"gray",board,isKing)
    return currentPlayer,opposingPlayer,currentPlayerTokens,opposingPlayerTokens,forwardRowInc

def win(board):
    rCount=0
    bCount=0
    for row in board:
        for col in row:
            if col in ['r','R']:
                rCount+=1
            elif col in ['b','B']:
                bCount+=1
    if rCount==0:
        return [True,"black"]
    if bCount==0:
        return [True,"red"]
    return [False,""]

def saveGame(board,currentPlayer):
    answer=input("Enter file name to save game, or hit enter to quit => ")
    if answer != "":
        outFile=open(answer,"w")
        outFile.write(currentPlayer+"\n")
        for row in board:
            outRow=""
            for token in row:
                if token=="":
                    outRow=outRow+"e"
                else:
                    outRow=outRow+token
            outFile.write(outRow+"\n")
        outFile.close()
    
def checkers():
    t,wn,board=setupBoard()
    gameName=input("Press enter to start a new game, otherwise, type in the name of an old game => ") 
    if gameName!="":
        currentPlayer,opposingPlayer,currentPlayerTokens,opposingPlayerTokens,forwardRowInc=oldGame(t,wn,board,gameName)
    else:
        currentPlayer,opposingPlayer,currentPlayerTokens,opposingPlayerTokens,forwardRowInc=newGame(t,wn,board)
    move=getValidPlayerAction(currentPlayer,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc)
    while move != "QUIT" and not win(board)[0]:
        fromRow,fromCol,toRow,toCol=parseValidMove(move)
        isKing = removeChecker(t,wn,fromRow,fromCol,board)
        drawChecker(t,wn,toRow,toCol,currentPlayer,"gray",board,isKing)
        if abs(fromRow-toRow)>1: #Jump is occuring
            removeChecker(t,wn,(fromRow+toRow)//2,(fromCol+toCol)//2,board)
        currentPlayer,currentPlayerTokens,opposingPlayer,opposingPlayerTokens,forwardRowInc=switchPlayer(currentPlayer)
        if not win(board)[0]:
            move=getValidPlayerAction(currentPlayer,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc)
    if move=="QUIT":
        saveGame(board,currentPlayer)


checkers()
