import random

"""
1) If a move to the King row with a regular checker is available, take it so
the checker will become a King
2) If a move to a side square is available, take it
3) If a jump to a King row with a regular checker is available, take it so
the checker will become a king
4) If multiple jumps are available, take the longest jump.  If all jumps are
equal length, take the jump that lands closest to the opposing home row.
5) A heuristic of your own choosing
"""

def listValidMoves(board,currentPlayerTokens,rowInc):
    validMovesList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if board[row][col] in ['r','b']: #regular checkers
                    for colInc in [1,-1]:
                        if row+rowInc>=0 and row+rowInc <=7 \
                           and col+colInc>=0 and col+colInc<=7 \
                           and board[row+rowInc][col+colInc]=="":
                            validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
                else: #king
                    for rInc in [1,-1]:
                        for cInc in [-1,1]:
                            if (col+cInc)>=0 and (col+cInc)<=7 \
                              and (row+rInc)>=0 and (row+rInc)<=7 \
                              and board[row+rInc][col+cInc]=="":
                                validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rInc+65)+str(col+cInc))                       
    return validMovesList

#function to return a list of all valid jumps for the current player
def listValidSingleJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens): #Not finished
    validSingleJumpsList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if board[row][col] in ['r','b']: #regular cheecker
                    for colInc in [1,-1]:
                        if row+rowInc*2>=0 and row+rowInc*2<=7 and \
                           col+colInc*2>=0 and col+colInc*2<=7 and \
                           board[row+rowInc][col+colInc] in opposingPlayerTokens and \
                           board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                            validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+2*rowInc+65)+str(col+colInc*2))
                else: #king checker
                    for rInc in [1,-1]:
                        for cInc in [-1,1]:
                            if (col+cInc)>=0 and (col+cInc)<=7 and \
                               (row+rInc)>=0 and (row+rInc)<=7 and \
                               board[row+rInc][col+cInc] in opposingPlayerTokens and \
                               (col+2*cInc)>=0 and (col+2*cInc)<=7 \
                               and row+(2*rInc)>=0 and row+(2*rInc)<=7 \
                               and board[row+(2*rInc)][col+(2*cInc)]=='' : 
                                validSingleJumpsList.append(chr(row+65)+str(col)+":"+chr(row+(2*rInc)+65)+str(col+(2*cInc)))                            
    return validSingleJumpsList

def expandJumps(board,player,oldJumps,playerTokens,opponentTokens,rowInc):
    VALID_RANGE=range(8)
    newJumps=[]
    for oldJump in oldJumps:
        row=ord(oldJump[-2])-65
        col=int(oldJump[-1])
        newJumps.append(oldJump)
        startRow=ord(oldJump[0])-65
        startCol=int(oldJump[1])
        if board[startRow][startCol] not in ['R','B']: #not a king
            for colInc in [1,-1]:
                jumprow=row+rowInc
                jumpcol=col+colInc
                torow=row+2*rowInc
                tocol=col+2*colInc
                if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                and board[jumprow][jumpcol] in opponentTokens and board[torow][tocol]=="":
                    newJumps.append(oldJump+":"+chr(torow+65)+str(tocol))
                    if oldJump in newJumps:
                        newJumps.remove(oldJump)
        else: #is a king
            for colInc in [1,-1]:
                for newRowInc in [1,-1]:
                    jumprow=row+newRowInc
                    jumpcol=col+colInc
                    torow=row+2*newRowInc
                    tocol=col+2*colInc
                    if jumprow in VALID_RANGE and jumpcol in VALID_RANGE and torow in VALID_RANGE and tocol in VALID_RANGE \
                    and board[jumprow][jumpcol] in opponentTokens and (board[torow][tocol]=="" or oldJump[0:2]==chr(torow+65)+str(tocol)) \
                    and ((oldJump[-2:]+":"+chr(torow+65)+str(tocol)) not in oldJump) and ((chr(torow+65)+str(tocol)+':'+oldJump[-2:] not in oldJump)) and (chr(torow+65)+str(tocol)!=oldJump[-5:-3]):
                        newJumps.append(oldJump+":"+chr(torow+65)+str(tocol))
                        if oldJump in newJumps:
                            newJumps.remove(oldJump)
    return newJumps 

#Heuristic 1
def MoveRegularCheckerToKingRow(validMovesList,kingRow,board):
    move=""
    choiceList=[]
    for possible in validMovesList:
        if int(ord(possible[3])-65)==kingRow and board[ord(possible[0])-65][int(possible[1])] in ['r','b']:
            choiceList.append(possible)
    if choiceList!=[]:
        move=choiceList[random.randrange(len(choiceList))]
    return move

#Heuristic 2
def MoveAnyToSideSquare(validMovesList):
    move=""
    choiceList=[]
    for possible in validMovesList:
        if int(possible[4])==0 or int(possible[4])==7:
            choiceList.append(possible)
    if choiceList!=[]:
        move=choiceList[random.randrange(len(choiceList))]
    return move

#Heuristic 3
def JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board):
    jump=""
    choiceList=[]
    for possible in expandedJumpsList:
        if int(ord(possible[-2])-65)==kingRow and board[ord(possible[0])-65][int(possible[1])] in ['r','b']:
            choiceList.append(possible)
    if choiceList!=[]:
        jump=choiceList[random.randrange(len(choiceList))]
    return jump

#Heuristic 4
def JumpTakeLongestOrFurthest(expandedJumpsList,kingRow):
    jump=""
    choiceList=[]
    if expandedJumpsList!=[]:
        #Check for longest
        maxLen=len(expandedJumpsList[0])
        for item in expandedJumpsList:
            if len(item)>maxLen:
                maxLen=len(item)
        for item in expandedJumpsList:
            if len(item)==maxLen:
                choiceList.append(item)
        if len(choiceList)!=1:
            minDist=abs(ord(expandedJumpsList[0][-2])-65-kingRow)
            for item in expandedJumpsList:
                if abs(ord(item[-2])-65-kingRow)<minDist:
                    minDist=abs(ord(item[-2])-65-kingRow)
            for item in expandedJumpsList:
                if abs(ord(item[-2])-65-kingRow)==minDist:
                    choiceList.append(item)
        if choiceList!=[]:
            jump=choiceList[random.randrange(len(choiceList))]
    return jump

     
#Heuristic 5
def keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList):
    otherJumps = False
    otherMoves = False
    for jump in expandedJumpsList:
        if jump[0] != "H":
            otherJumps = True
            
    for move in validMovesList:
        if move[0] != "H":
            otherMoves = True
            
    for jump in expandedJumpsList:
        if jump[0] == "H" and otherJumps == False:
            return jump
            
    for move in validMovesList:
        if move[0] == "H" and otherMoves == False:
            return move
            
    return ""

#Heuristic 6
def moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList):
    for move in expandedJumpsList:
        if move[3:] == "E3" or move[3:] == "D4":
            return move
    for move in validMovesList:
        if move[3:] == "E3" or move[3:] == "D4":
            return move
    return ""

#Heuristic 7
def tradeCheckers(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,expandedOpposingJumpsList):
    currentCount = 0
    opposingCount = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                currentCount += 1
            elif board[row][col] in opposingPlayerTokens:
                opposingCount += 1
    if currentCount > opposingCount:
        for jump in expandedJumpsList:
            if len(jump) == 5:
                for step in expandedOpposingJumpsList:
                    if jump[3:] == step[3:]:
                        return jump
    return ""
    
def getValidPlayerAction(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc):
    #Prepare lists for move selection
    if forwardRowInc==-1:
        kingRow=0
    else:
        kingRow=7
    validMovesList=listValidMoves(board,currentPlayerTokens,forwardRowInc)
    validOpponentMovesList = listValidMoves(board,opposingPlayerTokens,forwardRowInc*-1)
    print("Valid Moves List",validMovesList)
    validSingleJumpsList=listValidSingleJumps(board,currentPlayerTokens,forwardRowInc,opposingPlayerTokens)
    validOpposingSingleJumpsList=listValidSingleJumps(board,opposingPlayerTokens,forwardRowInc*-1,opposingPlayerTokens)
    
    print("Valid Single Jumps List",validSingleJumpsList)
    oldJumpsList=validSingleJumpsList
    oldJumpsList2=validOpponentMovesList
    expandedJumpsList=expandJumps(board,player,oldJumpsList,currentPlayerTokens,opposingPlayerTokens,forwardRowInc)
    expandedOpposingJumpsList=expandJumps(board,player,oldJumpsList2,currentPlayerTokens,opposingPlayerTokens,forwardRowInc*-1)
    #These are the lists of opposing player moves
    print("ValidMovesList:",validMovesList)
    print("validOpponentMovesList:",validOpponentMovesList)
    print("validSingleJumpsList:",validSingleJumpsList)
    print("validOpposingSingleJumpsList:",validOpposingSingleJumpsList)
    print("expandedJumpsList:",expandedJumpsList)
    print("expandedOpposingJumpsList:",expandedOpposingJumpsList)
    while expandedJumpsList != oldJumpsList:
        oldJumpsList=expandedJumpsList
        expandedJumpsList=expandJumps(board,player,oldJumpsList,currentPlayerTokens,opposingPlayerTokens,forwardRowInc)
    print("Expanded Jumps List",expandedJumpsList)
    print("Opposing player actions:",listValidMoves(board,opposingPlayerTokens,forwardRowInc*-1))
    
    #Decide on move
    if len(expandedJumpsList)>0:  #JUMP MUST BE TAKEN
        if tradeCheckers(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,expandedOpposingJumpsList) != "":
            input("Press enter to make this move or a similar one " + tradeCheckers(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,expandedOpposingJumpsList))
            return tradeCheckers(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,expandedOpposingJumpsList)
        if JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board) !="":
            input("Press enter to make this move or a similar one " + JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board))
            return JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board)
        if JumpTakeLongestOrFurthest(expandedJumpsList,kingRow) !="":
            input("Press enter to make this move or a similar one " + JumpTakeLongestOrFurthest(expandedJumpsList,kingRow))
            return JumpTakeLongestOrFurthest(expandedJumpsList,kingRow)
##        move=expandedJumpsList[0]
        move=input("Enter jump for player "+player+" => ").upper()
        while move != "QUIT" and move not in expandedJumpsList:
            print("Must take a jump . . .  try again!")
            move=input("Enter jump for player "+player+" => ").upper()
    else: #Select a Move
        if moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList) != "":
            input("Press enter to make this move or a similar one " + moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList))
            return moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList)
        if keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList) !="":
            input("Press enter to make this move or a similar one " + keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList))
            return keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList)
        if MoveRegularCheckerToKingRow(validMovesList,kingRow,board) !="":
            input("Press enter to make this move or a similar one " + MoveRegularCheckerToKingRow(validMovesList,kingRow,board))
            return MoveRegularCheckerToKingRow(validMovesList,kingRow,board)
        if MoveAnyToSideSquare(validMovesList) !="":
            input("Press enter to make this move or a similar one " + MoveAnyToSideSquare(validMovesList))
            return MoveAnyToSideSquare(validMovesList)
##        move=validMovesList[0]
        move=input("Enter move for player "+player+" => ").upper()
        while move != "QUIT" and move not in validMovesList:
            print("Bad move . . .  try again!")
            move=input("Enter move for player "+player+" => ").upper()
    return move

