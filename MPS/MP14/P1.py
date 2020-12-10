import random
import copy

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

def parseValidMove(move):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    move=move[3:]
    return move,fromRow,fromCol,toRow,toCol

#Heuristic 1 - Move a normal checker to the king row
def MoveRegularCheckerToKingRow(validMovesList,kingRow,board):
    move=""
    choiceList=[]
    for possible in validMovesList:
        if int(ord(possible[3])-65)==kingRow and board[ord(possible[0])-65][int(possible[1])] in ['r','b']:
            choiceList.append(possible)
    if choiceList!=[]:
        move=choiceList[random.randrange(len(choiceList))]
    return move

#Heuristic 2 - Move to the side square
def MoveNonKingToSideSquare(validMovesList,board):
    move=""
    choiceList=[]
    for possible in validMovesList:
        if (int(possible[4])==0 or int(possible[4])==7) and board[ord(possible[0])-65][int(possible[1])] not in ['R','B']:
            choiceList.append(possible)
    if choiceList!=[]:
        move=choiceList[random.randrange(len(choiceList))]
    return move

#Heuristic 3 - Jump to the king row if possible
def JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board):
    jump=""
    choiceList=[]
    for possible in expandedJumpsList:
        if int(ord(possible[-2])-65)==kingRow and board[ord(possible[0])-65][int(possible[1])] in ['r','b']:
            choiceList.append(possible)
    if choiceList!=[]:
        jump=choiceList[random.randrange(len(choiceList))]
    return jump

#Heuristic 4 - Take farthest jump to end row or take longest jump chain
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


#Heuristic 5 Uses my information and the potential jumps of the opponent to pick a blocking jump
def blockOpponentJumpWithJump(expandedJumpsList,opponentExpandedJumpsList):
    blockingJumps=[]
    for otherJump in opponentExpandedJumpsList:
        for myJump in expandedJumpsList:
            if otherJump[-2:] == myJump[-2:]:
                blockingJumps.append(myJump)
    if len(blockingJumps) > 0:
        return blockingJumps
    else:
        return 0


#Heuristic 6 Uses potential jumps by opponent and looks for blocking moves
def blockOpponentJumpWithMove(opponentExpandedJumpsList,validMovesList):
    blockingMoves=[]
    for jump in opponentExpandedJumpsList:
        for move in validMovesList:
            if jump[3:] == move[3:]:
                blockingMoves.append(move)
    if len(blockingMoves) > 0:
        return blockingMoves
    else:
        return ""
    #I already wrote these heuristics sadly...
    return blockingMoves[0]

#Heuristic 7 - pick a move that does not place in jump jeopardy
def moveNoJumpJeopardy(player,board,validMovesList,originalOpponentExpandedJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc):
    #print("IN moveNoJumpJeopardy")
    safeMoves=[]
    blockingMoves=[]
    #print("VALID MOVES LIST",validMovesList)
    for mv in validMovesList:
        #copy board
        dummyBoard=copy.deepcopy(board)
        #get locations for potential moves
        junk,fromRow,fromCol,toRow,toCol=parseValidMove(mv)
        #make this move in dummy board
        dummyBoard[toRow][toCol]=dummyBoard[fromRow][fromCol]
        dummyBoard[fromRow][fromCol]=""
        #pass dummy board to enemy jump expansion
        opponentValidSingleJumpsList=listValidSingleJumps(dummyBoard,opposingPlayerTokens,forwardRowInc*-1,currentPlayerTokens)
        opponentOldJumpsList=opponentValidSingleJumpsList[:]
        if player=="black":
            opposingPlayer="red"
        else:
            opposingPlayer="black"
        opponentExpandedJumpsList=expandJumps(dummyBoard,opposingPlayer,opponentOldJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc*-1)
        while opponentExpandedJumpsList != opponentOldJumpsList:
            opponentOldJumpsList=opponentExpandedJumpsList[:]
            opponentExpandedJumpsList=expandJumps(dummyBoard,opposingPlayer,opponentOldJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc*-1)  
        #if new jump expansion list is same as old, mv must not be jumpable
        if originalOpponentExpandedJumpsList==opponentExpandedJumpsList:
            safeMoves.append(mv)
        elif len(originalOpponentExpandedJumpsList)>len(opponentExpandedJumpsList):
            blockingMoves.append(mv)
    #print("SAFEMOVES ARE:",safeMoves)
    #print("BLOCKING MOVES ARE:",blockingMoves)
    #if len(safeMoves)>0 or len(blockingMoves) >0:
    #    input("Press enter to continue")
    if len(blockingMoves)>0:
        return blockingMoves[random.randrange(len(blockingMoves))]
    if len(safeMoves)>0:
        return safeMoves[random.randrange(len(safeMoves))]
    return ""
   
#Heuristic 8 - If player is winning, it always trades a checker when available, meaning makes a jump where they can be jumped so that both players lose a checker.
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
   
#Heuristic 9 - If it's possible to move to one of the center four squares it always does. Controlling the middle of the board is key in checkers.
def moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList):
    for move in expandedJumpsList:
        if move[3:] == "E3" or move[3:] == "D4":
            return move
    for move in validMovesList:
        if move[3:] == "E3" or move[3:] == "D4":
            return move
    return ""
   
#Heuristic 10 - Keep the last row if possible.
def keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList):
    otherJumps = False
    otherMoves = False
    for jump in expandedJumpsList:
        if jump[0] != "H" or jump[0] != "A":
            otherJumps = True
           
    for move in validMovesList:
        if move[0] != "H" or move[0] != "A":
            otherMoves = True
           
    for jump in expandedJumpsList:
        if (jump[0] == "H" or jump[0] != "A") and otherJumps == False:
            return jump
           
    for move in validMovesList:
        if (move[0] == "H" or jump[0] != "A") and otherMoves == False:
            return move
           
    return ""

#Heuristic 11 - If the current player is winning on peice count, act normally (i.e, be okay with trades). If
#the current player is losing in terms of peice count, don't move into a position where you can be jumped,
#even if just for a trade, next turn.
def dontSacrifice(player,currentPlayerTokens,opposingPlayerTokens,board,validOpponentMovesList,validMovesList):
    shouldTrade = False
    rCount=0
    bCount=0
    for row in board:
        for col in row:
            if col in ['r','R']:
                rCount+=1
            elif col in ['b','B']:
                bCount+=1
    if rCount > bCount:
        shouldTrade = False
    else:
        shouldTrade = True
    dontMoveList = []
    if shouldTrade == False:
        for p2Move in validOpponentMovesList:
            for aiMove in validMovesList:
                if p2Move[3:] == aiMove[3:]:
                    dontMoveList.append(aiMove)
        for move in validMovesList:
            if move in dontMoveList:
                validMovesList.remove(move)
    if len(validMovesList)>0:
        return validMovesList[0]
    else:
        return ""
       
#Heuristic 12 - Moves pieces forward together in a pyramid/triangle formation
def keepStrongFormation(currentPlayerTokens,opposingPlayerTokens,board,validMovesList):
    farthestChecker = 0
    foundFarthest = False
 
    if currentPlayerTokens == ['r','R']:
        for row in range(6):
            for col in range(8):
                if board[row][col] in currentPlayerTokens and foundFarthest == False and board[row-2][col] in currentPlayerTokens:
                    farthestChecker = row
                    foundFarthest = True
                   
        for col in range(8):
            if board[farthestChecker-1][col] == "":
                for move in validMovesList:
                    if move[0] != 'A' and move[3] == chr(65 + farthestChecker - 1):
                        if col == 0:
                            if board[farthestChecker][col+1] not in opposingPlayerTokens:
                                return move
                        elif col == 8:
                            if board[farthestChecker][col-1] not in opposingPlayerTokens:
                                return move
                        else:
                            if board[farthestChecker][col+1] not in opposingPlayerTokens and board[farthestChecker][col-1] not in opposingPlayerTokens:
                                return move
        return ""
    else:
        for row in range(6):
            for col in range(8):
                if board[row][col] in currentPlayerTokens and foundFarthest == False and board[row+2][col] in currentPlayerTokens:
                    farthestChecker = row
                    foundFarthest = True
                   
        for col in range(8):
            if board[farthestChecker+1][col] == "":
                for move in validMovesList:
                    if move[0] != 'H' and move[3] == chr(65 + farthestChecker + 1):
                        if col == 0:
                            if board[farthestChecker][col+1] not in opposingPlayerTokens:
                                return move
                        elif col == 8:
                            if board[farthestChecker][col-1] not in opposingPlayerTokens:
                                return move
                        else:
                            if board[farthestChecker][col+1] not in opposingPlayerTokens and board[farthestChecker][col-1] not in opposingPlayerTokens:
                                return move
        return ""
def getValidPlayerAction(PRINT_DEBUG,player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc):
    #Prepare lists for move selection
    if forwardRowInc==-1:
        kingRow=0
    else:
        kingRow=7
       
    #My possible moves
    validMovesList=listValidMoves(board,currentPlayerTokens,forwardRowInc)
    #print("Valid Moves List",validMovesList)
    validSingleJumpsList=listValidSingleJumps(board,currentPlayerTokens,forwardRowInc,opposingPlayerTokens)
    if PRINT_DEBUG:print("Valid Single Jumps List",validSingleJumpsList)
    oldJumpsList=validSingleJumpsList[:]
    expandedJumpsList=expandJumps(board,player,oldJumpsList,currentPlayerTokens,opposingPlayerTokens,forwardRowInc)
    while expandedJumpsList != oldJumpsList:
        oldJumpsList=expandedJumpsList[:]
        expandedJumpsList=expandJumps(board,player,oldJumpsList,currentPlayerTokens,opposingPlayerTokens,forwardRowInc)
    if PRINT_DEBUG:print("Expanded Jumps List",expandedJumpsList)

    #Opposing player possible moves
    opponentValidMovesList=listValidMoves(board,opposingPlayerTokens,forwardRowInc*-1)
    if PRINT_DEBUG:print("Opponent Valid Moves List",opponentValidMovesList)
    opponentValidSingleJumpsList=listValidSingleJumps(board,opposingPlayerTokens,forwardRowInc*-1,currentPlayerTokens)
    if PRINT_DEBUG:print("Opponent Valid Single Jumps List",opponentValidSingleJumpsList)
    opponentOldJumpsList=opponentValidSingleJumpsList[:]
    if player=="black":
        opposingPlayer="red"
    else:
        opposingPlayer="black"
    opponentExpandedJumpsList=expandJumps(board,opposingPlayer,opponentOldJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc*-1)
    while opponentExpandedJumpsList != opponentOldJumpsList:
        opponentOldJumpsList=opponentExpandedJumpsList[:]
        opponentExpandedJumpsList=expandJumps(board,opposingPlayer,opponentOldJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc*-1)
    if PRINT_DEBUG:print("Expanded Jumps List",expandedJumpsList)
    if PRINT_DEBUG:input("Press enter to continue ")
   
    #Decide on jump
    if len(expandedJumpsList)>0:  #JUMP MUST BE TAKEN
        jmp = blockOpponentJumpWithJump(expandedJumpsList,opponentExpandedJumpsList)
        jmp = tradeCheckers(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,opponentExpandedJumpsList)
        jmp=JumpToKingRowRegularChecker(expandedJumpsList,kingRow,board)
        if jmp!="":
            #input("Press enter to make this move " + jmp)
            return jmp
        jmp=JumpTakeLongestOrFurthest(expandedJumpsList,kingRow)
        if jmp!="":
            #input("Press enter to make this move " + jmp)
            return jmp
        move=expandedJumpsList[0] #[random.randrange(len(expandedJumpsList))]
##        move=input("Enter jump for player "+player+" => ").upper()
##        while move != "QUIT" and move not in expandedJumpsList:
##            print("Must take a jump . . .  try again!")
##            move=input("Enter jump for player "+player+" => ").upper()
    else: #Select a Move
        mv=moveNoJumpJeopardy(player,board,validMovesList,opponentExpandedJumpsList,opposingPlayerTokens,currentPlayerTokens,forwardRowInc)
        if mv!="":return mv
        mv = blockOpponentJumpWithMove(opponentExpandedJumpsList,validMovesList)
        if mv!="":return mv
        #mv = keepLastRow(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc, validMovesList, expandedJumpsList)
        #if mv!="":return mv
        mv = dontSacrifice(player,currentPlayerTokens,opposingPlayerTokens,board,opponentValidMovesList,validMovesList)
        if mv!="":return mv
        mv=MoveRegularCheckerToKingRow(validMovesList,kingRow,board)
        if mv!="":return mv
        mv=MoveNonKingToSideSquare(validMovesList,board)
        if mv!="":return mv
        mv = moveToMiddle(player,currentPlayerTokens,opposingPlayerTokens,board,forwardRowInc,expandedJumpsList,validMovesList)
        if mv!="":return mv
        mv = keepStrongFormation(currentPlayerTokens,opposingPlayerTokens,board,validMovesList)
        if mv!="":return mv
        if validMovesList==[]:return "QUIT"
        move=validMovesList[random.randrange(len(validMovesList))]
##        move=input("Enter move for player "+player+" => ").upper()
##        while move != "QUIT" and move not in validMovesList:
##            print("Bad move . . .  try again!")
##            move=input("Enter move for player "+player+" => ").upper()
    return move