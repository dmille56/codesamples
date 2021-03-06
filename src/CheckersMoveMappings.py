import Queue

#this file contains the move/jump mappings for each space on the board

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

#set the distance mappings (the distance in moves between every space in the
#board)... we're using djkstra's algorithm to do this
def updateDistanceMappings(distMapping, moveMapping, i):
    visited = [False for x in range(33)]

    distMapping[i] = {}
    for j in range(1, 33):
        distMapping[i][j] = float("inf")

    queue = Queue.PriorityQueue()
    queue.put((0, i))
    while(not queue.empty()):
        moves, j = queue.get()
        if(visited[j] == True):
            next
        visited[j] = True
        distMapping[i][j] = min(distMapping[i][j], moves)

        for m in moveMapping[j]:
            if(visited[m] == False):
                queue.put((moves+1, m))

blackDistanceMapping = {}
for i in range(1, 33):
    updateDistanceMappings(blackDistanceMapping, blackMoveMapping, i)

whiteDistanceMapping = {}
for i in range(1, 33):
    updateDistanceMappings(whiteDistanceMapping, whiteMoveMapping, i)

kingDistanceMapping = {}
for i in range(1, 33):
    updateDistanceMappings(kingDistanceMapping, kingMoveMapping, i)

distanceMappings = {'w':whiteDistanceMapping, 'b':blackDistanceMapping}
