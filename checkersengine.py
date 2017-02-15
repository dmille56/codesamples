import re, tkFont, copy, random, time, tkMessageBox
from Tkinter import *
from functools import partial
import cPickle as pickle

#the squares that a checker can move into from each position
blackMoveMapping = {1:[5, 6],
                    2:[6, 7],
                    3:[7, 8],
                    4:[8],
                    5:[9],
                    6:[9, 10],
                    7:[10, 11],
                    8:[11, 12],
                    9:[13, 14],
                    10:[14, 15],
                    11:[15, 16],
                    12:[16],
                    13:[17],
                    14:[17, 18],
                    15:[18, 19],
                    16:[19, 20],
                    17:[21, 22],
                    18:[22, 23],
                    19:[23, 24],
                    20:[24],
                    21:[25],
                    22:[25, 26],
                    23:[26, 27],
                    24:[27, 28],
                    25:[29, 30],
                    26:[30, 31],
                    27:[31, 32],
                    28:[32],
                    29:[],
                    30:[],
                    31:[],
                    32:[]}

whiteMoveMapping = {1:[],
                    2:[],
                    3:[],
                    4:[],
                    5:[1],
                    6:[1, 2],
                    7:[2, 3],
                    8:[3, 4],
                    9:[5, 6],
                    10:[6, 7],
                    11:[7, 8],
                    12:[8],
                    13:[9],
                    14:[9, 10],
                    15:[10, 11],
                    16:[11, 12],
                    17:[13, 14],
                    18:[14, 15],
                    19:[15, 16],
                    20:[16],
                    21:[17],
                    22:[17, 18],
                    23:[18, 19],
                    24:[19, 20],
                    25:[21, 22],
                    26:[22, 23],
                    27:[23, 24],
                    28:[24],
                    29:[25],
                    30:[25, 26],
                    31:[26, 27],
                    32:[27, 28]}

# in each list(for each position) first is the piece to be jumped over, second is
# the landing spot 
blackJumpMapping = {1:[[6, 10]],
                    2:[[6, 9], [7, 11]],
                    3:[[7, 10], [8, 12]],
                    4:[[8, 11]],
                    5:[[9, 14]],
                    6:[[9, 13], [10, 15]],
                    7:[[10, 14], [11, 16]],
                    8:[[11, 15]],
                    9:[[14, 18]],
                    10:[[14, 17], [15, 19]],
                    11:[[15, 18], [16, 20]],
                    12:[[16, 19]],
                    13:[[17, 22]],
                    14:[[17, 21], [18, 23]],
                    15:[[18, 22], [19, 24]],
                    16:[[19, 23]],
                    17:[[22, 26]],
                    18:[[22, 25], [23, 27]],
                    19:[[23, 26], [24, 28]],
                    20:[[24, 27]],
                    21:[[25, 30]],
                    22:[[25, 29], [26, 31]],
                    23:[[26, 30], [27, 32]],
                    24:[[27, 31]],
                    25:[],
                    26:[],
                    27:[],
                    28:[],
                    29:[],
                    30:[],
                    31:[],
                    32:[]}

whiteJumpMapping = {1:[],
                    2:[],
                    3:[],
                    4:[],
                    5:[],
                    6:[],
                    7:[],
                    8:[],
                    9:[[6, 2]],
                    10:[[6, 1], [7, 3]],
                    11:[[7, 2], [8, 4]],
                    12:[[8, 3]],
                    13:[[9, 6]],
                    14:[[9, 5], [10, 7]],
                    15:[[10, 6], [11, 8]],
                    16:[[11, 7]],
                    17:[[14, 10]],
                    18:[[14, 9], [15, 11]],
                    19:[[15, 10], [16, 12]],
                    20:[[16, 11]],
                    21:[[17, 14]],
                    22:[[17, 13], [18, 15]],
                    23:[[18, 14], [19, 16]],
                    24:[[19, 15]],
                    25:[[22, 18]],
                    26:[[22, 17], [23, 19]],
                    27:[[23, 18], [24, 20]],
                    28:[[24, 19]],
                    29:[[25, 22]],
                    30:[[25, 21], [26, 23]],
                    31:[[26, 22], [27, 24]],
                    32:[[27, 23]]}

kingMoveMapping =  {1:[5, 6],
                    2:[6, 7],
                    3:[7, 8],
                    4:[8],
                    5:[1, 9],
                    6:[1, 2, 9, 10],
                    7:[2, 3, 10, 11],
                    8:[3, 4, 11, 12],
                    9:[5, 6, 13, 14],
                    10:[6, 7, 14, 15],
                    11:[7, 8, 15, 16],
                    12:[8, 16],
                    13:[9, 17],
                    14:[9, 10, 17, 18],
                    15:[10, 11, 18, 19],
                    16:[11, 12, 19, 20],
                    17:[13, 14, 21, 22],
                    18:[14, 15, 22, 23],
                    19:[15, 16, 23, 24],
                    20:[16, 24],
                    21:[17, 25],
                    22:[17, 18, 25, 26],
                    23:[18, 19, 26, 27],
                    24:[19, 20, 27, 28],
                    25:[21, 22, 29, 30],
                    26:[22, 23, 30, 31],
                    27:[23, 24, 31, 32],
                    28:[24, 32],
                    29:[25],
                    30:[25, 26],
                    31:[26, 27],
                    32:[27, 28]}

kingJumpMapping =  {1:[[6, 10]],
                    2:[[6, 9], [7, 11]],
                    3:[[7, 10], [8, 12]],
                    4:[[8, 11]],
                    5:[[9, 14]],
                    6:[[9, 13], [10, 15]],
                    7:[[10, 14], [11, 16]],
                    8:[[11, 15]],
                    9:[[6, 2], [14, 18]],
                    10:[[6, 1], [7, 3], [14, 17], [15, 19]],
                    11:[[7, 2], [8, 4], [15, 18], [16, 20]],
                    12:[[8, 3], [16, 19]],
                    13:[[9, 6], [17, 22]],
                    14:[[9, 5], [10, 7], [17, 21], [18, 23]],
                    15:[[10, 6], [11, 8], [18, 22], [19, 24]],
                    16:[[11, 7], [19, 23]],
                    17:[[14, 10], [22, 26]],
                    18:[[14, 9], [15, 11], [22, 25], [23, 27]],
                    19:[[15, 10], [16, 12], [23, 26], [24, 28]],
                    20:[[16, 11], [24, 27]],
                    21:[[17, 14], [25, 30]],
                    22:[[17, 13], [18, 15], [25, 29], [26, 31]],
                    23:[[18, 14], [19, 16], [26, 30], [27, 32]],
                    24:[[19, 15], [27, 31]],
                    25:[[22, 18]],
                    26:[[22, 17], [23, 19]],
                    27:[[23, 18], [24, 20]],
                    28:[[24, 19]],
                    29:[[25, 22]],
                    30:[[25, 21], [26, 23]],
                    31:[[26, 22], [27, 24]],
                    32:[[27, 23]]}

moveMappings = {'w':whiteMoveMapping, 'b':blackMoveMapping}
jumpMappings = {'w':whiteJumpMapping, 'b':blackJumpMapping}

weightsFileName = 'weights.p'

learnConstant = 0.1 #learning constant
initialWeight = 0.5

#0 == empty
#1 == black checker
#2 == black king
#3 == white checker
#4 == white king
def makeBoard():
    board = [0 for x in range(32)]
    for i in range(12):
        board[i] = 3
    for i in range(20, 32):
        board[i] = 1

    return board

def makeInitialWeights():
    weights = []
    for i in range(4):
        a = [initialWeight for j in range(32)]
        weights.append(a)
    return weights

def getFeatures(board):
    features = []
    for i in range(1, 5):
        a = [1 if(x == i) else 0 for x in board]
        features.append(a)
    return features

def evaluateFeatures(features, weights):
    value = 0
    for i in range(4):
        for j in range(32):
            value += (weights[i][j] * features[i][j])

    return value

def evaluateBoard(board, weights):
    return evaluateFeatures(getFeatures(board), weights)

def updateWeights(trainingData, weights, didWin):
    n = len(trainingData)
    estimates = [evaluateBoard(x, weights) for x in trainingData]
    values = [0 for x in range(n)]
    if(didWin == True):
        values[len(values)-1] = 100
    else:
        values[len(values)-1] = -100

    for i in range(n-1):
        values[i] = estimates[i+1]

    for i in range(n):
        board = trainingData[i]
        features = getFeatures(board)
        value = values[i]
        estimate = estimates[i] 

        #update our weights
        for j in range(len(weights)):
            for k in range(len(weights[j])):
                weights[j][k] = weights[j][k] + (learnConstant*(value-estimate)*features[j][k])


def getBestPossibleBoard(boards, weights):
    values = [evaluateBoard(b, weights) for b in boards]
    maxValue = values[0]
    maxBoard = boards[0]
    for i in range(1, len(boards)):
        if(values[i] > maxValue):
            maxValue = values[i]
            maxBoard = boards[i]

    return maxBoard

def getJumps(board, index, jumpMapping, enemyCheckers, prev, result):
    #i == the jumped over spot, j == the landing spot
    for (iK, jK) in jumpMapping[index+1]:
        i, j = iK-1, jK-1
        if(board[i] in enemyCheckers and board[j] == 0):
            at = copy.deepcopy(prev)
            at.append([i , j])
            result.append(at)
            getJumps(board, j, jumpMapping, enemyCheckers, at, result)

    return result 

def getKingJumps(board, index, allyKing, enemyCheckers, prev, result):
    for (iK, jK) in kingJumpMapping[index+1]:
        i, j = iK-1, jK-1
        if(board[i] in enemyCheckers and board[j] == 0):
            #set up the next board... we need to make sure the king can't jump
            #back over where it just jumped
            newBoard = copy.deepcopy(board)
            newBoard[index] = 0
            newBoard[i] = 0
            newBoard[j] = allyKing
            at = copy.deepcopy(prev)
            at.append([i, j])
            result.append(at)
            getKingJumps(newBoard, j, allyKing, enemyCheckers, at, result)

    return result 

def getAllPossibleJumps(board, turn):
    moves = []
    jumpMapping = jumpMappings[turn]

    allyChecker = 1 if(turn == 'w') else 3
    enemyChecker = 3 if(turn == 'w') else 1
    allyKing = 2 if(turn == 'w') else 4
    enemyKing = 4 if(turn == 'w') else 2
    enemyCheckers = [enemyChecker, enemyKing]

    for i in range(32):
        if(board[i] == allyChecker):
            at = getJumps(board, i, jumpMapping, enemyCheckers, [], [])
            if(at != []):
                for move in at:
                    moves.append([i, move])
        elif(board[i] == allyKing):
            at = getKingJumps(board, i, allyKing, enemyCheckers, [], [])
            if(at != []):
                for move in at:
                    moves.append([i, move])

    return moves

def getAllPossibleMoves(board, turn):
    moves = []
    moveMapping = moveMappings[turn]

    allyChecker = 1 if(turn == 'w') else 3
    enemyChecker = 3 if(turn == 'w') else 1
    allyKing = 2 if(turn == 'w') else 4
    enemyKing = 4 if(turn == 'w') else 2

    for i in range(32):
        if(board[i] == allyChecker):
            for j in moveMapping[i+1]:
                if(board[j-1] == 0):
                    moves.append([i, j-1])
        elif(board[i] == allyKing):
            for j in kingMoveMapping[i+1]:
                if(board[j-1] == 0):
                    moves.append([i, j-1])

    return moves

def crownPieces(board):
    for i in range(0, 4):
        if(board[i] == 1):
            board[i] = 2

    for i in range(28, 32):
        if(board[i] == 3):
            board[i] = 4

def getAllPossibleBoards(board, turn):
    boards = []
    jumps = getAllPossibleJumps(board, turn)
    if(jumps != []):
        for (i, moves) in jumps:
            newBoard = copy.deepcopy(board)
            for (j, k) in moves:
                newBoard[j] = 0
            newPosition = moves[len(moves)-1][1]
            newBoard[newPosition] = newBoard[i]
            newBoard[i] = 0
            crownPieces(newBoard)
            boards.append(newBoard)
    else:
        moves = getAllPossibleMoves(board, turn)
        for (i, j) in moves:
            newBoard = copy.deepcopy(board)
            newBoard[j] = newBoard[i]
            newBoard[i] = 0
            crownPieces(newBoard)
            boards.append(newBoard)

    return boards

def isGameOver(boards):
    return boards == []

def getRandomBoard(boards):
    randomNum = random.randint(0, len(boards)-1)
    return boards[randomNum]

#training our AI
iterations = 0
print("We will now train our AI using {0} iterations... this may take a while".format(iterations))

startTime = time.time()

#theWeights = pickle.load(open(weightsFileName, "rb")) 
#blackWeights, whiteWeights = theWeights

blackWeights = makeInitialWeights()
whiteWeights = makeInitialWeights()

#train the black AI against a random AI
for i in range(iterations):
    turn = 'b'
    board = makeBoard()
    boards = getAllPossibleBoards(board, turn)
    trainingData = []
    while(not isGameOver(boards)):
        if(turn == 'b'):
            bestBoard = getBestPossibleBoard(boards, blackWeights)
            board = bestBoard
            trainingData.append(board) 
            turn = 'w'
        else:
            randomBoard = getRandomBoard(boards)
            board = randomBoard
            turn = 'b'

        boards = getAllPossibleBoards(board, turn)

    didWin = (turn == 'w')
    updateWeights(trainingData, blackWeights, didWin)

#train the white AI against a random AI
for i in range(iterations):
    turn = 'b'
    board = makeBoard()
    boards = getAllPossibleBoards(board, turn)
    trainingData = []
    while(not isGameOver(boards)):
        if(turn == 'b'):
            randomBoard = getRandomBoard(boards)
            board = randomBoard
            turn = 'w'
        else:
            bestBoard = getBestPossibleBoard(boards, whiteWeights)
            board = bestBoard
            trainingData.append(board) 
            turn = 'b'

        boards = getAllPossibleBoards(board, turn)

    didWin = (turn == 'b')
    updateWeights(trainingData, whiteWeights, didWin)

print("--------------------")
print('blackWeights:')
print("--------------------")
print(blackWeights)
print("--------------------")
print('whiteWeights:')
print("--------------------")
print(whiteWeights)
print("--------------------")

#theWeights = [blackWeights, whiteWeights]
#pickle.dump(theWeights, open(weightsFileName, "wb")) 

endTime = time.time()
print("Training {0} iterations took: {1}".format(iterations, str(endTime-startTime)))

board = makeBoard()

# GUI Code

pieceSelected = False
currentTurn = 'b'
currentJumps = getAllPossibleJumps(board, 'b')
currentMoves = getAllPossibleMoves(board, 'b')
currentBoards = getAllPossibleBoards(board, 'b')
currentIndexes = {} 
currentGameOngoing = True
currentGameWinner = 'b'

def displayAllPossibleJumpsOrMoves(board, jumps, moves):
    if(jumps != []):
        for(i, moves) in jumps:
            buttons[i]['bg'] = 'green'
            for (j, k) in moves:
                buttons[j]['bg'] = 'red'
                buttons[k]['bg'] = 'blue'
    else:
        for (i, j) in moves:
            buttons[i]['bg'] = 'green'
            buttons[j]['bg'] = 'blue'

def displayPossibleJumpsOrMoves(board, jumps, moves, index):
    global currentIndexes
    currentIndexes = {}
    result = False
    if(jumps != []):
        for(i, moves) in jumps:
            if(i == index):
                result = True
                buttons[i]['bg'] = 'green'
                for (j, k) in moves:
                    buttons[j]['bg'] = 'red'
                    buttons[k]['bg'] = 'blue'
                    currentIndexes[k] = [i, moves] 
    else:
        for (i, j) in moves:
            if(i == index):
                result = True
                buttons[i]['bg'] = 'green'
                buttons[j]['bg'] = 'blue'
                currentIndexes[j] = [i]

    return result

def buttonClick(zeroIndex):
    global pieceSelected, currentIndexes, currentJumps, currentMoves
    global currentTurn, currentBoards, currentGameOngoing
    updateButtons(board)
    if(pieceSelected == True and zeroIndex in currentIndexes):
        pieceSelected = False
        startIndex = currentIndexes[zeroIndex][0]
        board[zeroIndex] = board[startIndex]
        board[startIndex] = 0

        #handle jumps
        if(len(currentIndexes[zeroIndex]) > 1):
            for (i, j) in currentIndexes[zeroIndex][1]:
                board[i] = 0
                if(board[j] == zeroIndex):
                    break

        crownPieces(board)
        updateButtons(board)
        if(currentTurn == 'b'):
            currentTurn = 'w'
        else:
            currentTurn = 'b'
        currentJumps = getAllPossibleJumps(board, currentTurn)
        currentMoves = getAllPossibleMoves(board, currentTurn)
        currentIndexes = {}
        currentBoards = getAllPossibleBoards(board, currentTurn)
        if(isGameOver(currentBoards)):
            winner = 'black' if(currentTurn == 'w') else 'white'
            tkMessageBox.showinfo('Game Over!', 'Game is over: {0} wins!'.format(winner))
            currentGameOngoing = False
    else:
        pieceSelected = displayPossibleJumpsOrMoves(board, currentJumps, currentMoves, zeroIndex)

root = Tk()

imagesFolder = 'checker_images'
separator = '/'
whiteCheckerImage = PhotoImage(file=imagesFolder + separator + 'whiteChecker.png')
blackCheckerImage = PhotoImage(file=imagesFolder + separator + 'blackChecker.png')
whiteCheckerKingImage = PhotoImage(file=imagesFolder + separator + 'whiteCheckerKing.png')
blackCheckerKingImage = PhotoImage(file=imagesFolder + separator + 'blackCheckerKing.png')
buttonUpdateImage = {0: '', 1:whiteCheckerImage, 2:whiteCheckerKingImage,
        3:blackCheckerImage, 4:blackCheckerKingImage}
def updateButtons(board):
    for i in range(32):
        buttons[i]['bg'] = 'grey'
        buttons[i].config(image=buttonUpdateImage[board[i]])

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
root.minsize(width=900, height=900)
root.maxsize(width=900, height=900)
root.wm_title("Checkers!!!")

frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

buttonFont = tkFont.Font(family='Helvetica', size=24, weight='bold')
buttons = []
i, j, num = 0, 0, 0
for r in range(8):
    num += 1
    if(num >= 2):
        num = 0
    for c in range(8):
        button = Button(frame, text="", command=partial(buttonClick, i)) 
        button.grid(row=r, column=c, sticky=N+S+E+W)
        button['font'] = buttonFont
        button['bg'] = 'white'
        button['state'] = 'disabled'
        button.config(height=100, width=100)
        if(j % 2 == num):
            i += 1
            #button['text'] = str(i) #this displays the index for each board position
            button['bg'] = 'grey'
            button['state'] = 'normal'
            buttons.append(button)

        j += 1

for r in range(8):
    Grid.rowconfigure(frame, r, weight=1)
for c in range(8):
    Grid.columnconfigure(frame, c, weight=1)

updateButtons(board)
root.mainloop()
