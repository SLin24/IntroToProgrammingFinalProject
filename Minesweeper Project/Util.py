from Constants import *
grid = [[-1 for i in range(x + 2)] for j in range(y + 2)]
neighborGrid = [[-1 for i in range(x+2)]for j in range(y+2)]
for i in range(x + 2):
    grid[0][i] = border
    neighborGrid[0][i] = border
    grid[y + 1][i] = border
    neighborGrid[y + 1][i] = border
for i in range(y + 2):
    grid[i][0] = border
    neighborGrid[i][0] = border
    grid[i][x + 1] = border
    neighborGrid[i][x + 1] = border



sources = [[0 for i in range(x)] for j in range(y)]

searchQueue = [[],[]]
visited = [[False for i in range(x + 2)] for j in range(y + 2)]
visitedNodes = [[False for i in range(x + 2)] for j in range(y + 2)]
curSearchQueue = 0
cnt = 0
# (row, col)
searchQueue[curSearchQueue].append((midY, midX))


print("INITIALIZATION")
# perhaps predefining each source?
for r in range(y):
    for c in range(x):
        targ = str(r + 1) + "_" + str(c + 1)
        sources[r][c] = driver.find_element("id", targ)


print("INITIALIZATION OVER")

def getCnt():
    return cnt

def reset():
    global cnt
    global grid
    global sources
    global searchQueue
    global visited
    global visitedNodes
    global curSearchQueue
    global neighborGrid

    grid = [[-1 for i in range(x + 2)] for j in range(y + 2)]
    neighborGrid = [[-1 for i in range(x+2)]for j in range(y+2)]
    for i in range(x + 2):
        grid[0][i] = border
        neighborGrid[0][i] = border
        grid[y + 1][i] = border
        neighborGrid[y + 1][i] = border
    for i in range(y + 2):
        grid[i][0] = border
        neighborGrid[i][0] = border
        grid[i][x + 1] = border
        neighborGrid[i][x + 1] = border


    searchQueue = [[],[]]
    visited = [[False for i in range(x + 2)] for j in range(y + 2)]
    visitedNodes = [[False for i in range(x + 2)] for j in range(y + 2)]
    curSearchQueue = 0
    # (row, col)
    searchQueue[curSearchQueue].append((midY, midX))
    cnt = 0






def flag(row, col):
    if (grid[row + 1][col + 1] != -1):
        return
    source = sources[row][col]
    grid[row + 1][col + 1] = -2
    action.context_click(source).perform()

def click(row, col):
    if (grid[row + 1][col + 1] != -1):
        return
    source = sources[row][col]
    action.click(source).perform()
    grid[row + 1][col + 1] = getSurroundings(row, col)

def getSurroundings(row, col):
    source = sources[row][col]
    tp = source.get_attribute("class")
    c = tp[11]
    if (c == 'k'):
        return -1
    elif (c == 'f'):
        return -2
    else:
        return int(c)
def check():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (grid[r][c] == -1):
                return False
    return True 

def start():
    click(midY, midX)


def periodicUpdate():
    global cnt
    change = False
    global curSearchQueue
    while (len(searchQueue[curSearchQueue]) > 0):
        front = searchQueue[curSearchQueue][0]
        searchQueue[curSearchQueue].pop(0)
        if (front[0] < 1 or front[0] >= y + 1 or front[1] < 1 or front[1] >= x + 1 or visited[front[0]][front[1]]):
            continue
        val = getSurroundings(front[0] - 1, front[1] - 1)
        if (val == -1):
            searchQueue[curSearchQueue ^ 1].append(front)
        else:
            change = True
            visited[front[0]][front[1]] = True
            cnt+=1
            grid[front[0]][front[1]] = val
            for i in range(4):
                searchQueue[curSearchQueue].append((front[0] + dY[i], front[1] + dX[i]))
    curSearchQueue ^= 1
    # for r in range(len(grid)):
    #     for c in range(len(grid[0])):
    #         if (grid[r][c] == -1):
    #             grid[r][c] = getSurroundings(r, c)
    #             if (grid[r][c] != -1): change = True
    return change
def basicMineFlag():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (grid[r][c] == -1 or grid[r][c] == -2 or grid[r][c] == border or visitedNodes[r][c]): continue
            neighbors = getNeighbors(r, c)
            neighborBlank = count(-1, neighbors)
            if (neighborBlank == 0):
                visitedNodes[r][c] = True
                continue
            mineFound = count(-2, neighbors)
            mineCnt = grid[r][c]
            if (mineCnt == mineFound + neighborBlank):
                flagAllNeighbors(neighbors)

def basicMineClick():
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if (grid[r][c] == -1 or grid[r][c] == -2 or visitedNodes[r][c]): continue
            neighbors = getNeighbors(r, c)
            mineFound = count(-2, neighbors)
            neighborBlank = count(-1, neighbors)
            mineCnt = grid[r][c]
            if (neighborBlank == 0):
                visitedNodes[r][c] = True
                continue
            if (mineFound == mineCnt):
                clickAllNeighbors(neighbors)


def flagAllNeighbors(neighbors):
    for point in neighbors:
        if (grid[point[0]][point[1]] == -1):
            flag(point[0] - 1, point[1] - 1)

def clickAllNeighbors(neighbors):
    for point in neighbors:
        if (grid[point[0]][point[1]] == -1):
            click(point[0] - 1, point[1] - 1)
                
def count(targ, neighbors):
    cnt = 0
    for point in neighbors:
        if (grid[point[0]][point[1]] == targ):
            cnt += 1
    return cnt

def getNeighbors(r, c):
    neighbors = []
    if (r > 1):
        neighbors.append((r - 1, c))
        if (c > 1):
            neighbors.append((r - 1, c - 1))
        if (c < len(grid[0]) - 2):
            neighbors.append((r - 1, c + 1))
    if (c > 1):
        neighbors.append((r, c - 1))
    if (c < len(grid[0]) - 2):
         neighbors.append((r, c + 1))
    if (r < len(grid) - 2):
        neighbors.append((r + 1, c))
        if (c > 1):
            neighbors.append((r + 1, c - 1))
        if (c < len(grid[0]) - 2):
            neighbors.append((r + 1, c + 1))

    return neighbors


# def search(pattern):

def encodePattern(pattern):
    transformedPattern = []
    for arr in pattern:
        line = ""
        for i in range(len(arr)):
           line += chr(97 + (arr[i] + 2))
        transformedPattern.append(line)
    return transformedPattern

# rotates pattern 90 degrees clockwise
def rotatePattern(pattern):
    ans = [[0 for i in range(len(pattern))] for j in range(len(pattern[0]))]
    
    for i in range(len(pattern[0])):
        for j in range(len(pattern)):
            ans[i][len(pattern) - 1 - j] = pattern[j][i]
    return ans

# rotates points
def rotateExcluded(pattern, rows, cols):
    ans = []
    for p in pattern:
        ans.append(rotatePoint(p, rows, cols))
    return ans
def rotatePoint(point, rows, cols):
    curPoint = (cols - 1 + point[1], rows - 1 + point[0])
    postPoint = (-curPoint[1], curPoint[0]) 
    postCorner = (0, cols - 1)
    return (postPoint[1] - postCorner[1], postPoint[0] - postCorner[0])    

# reflect pattern about y axis
def reflectPattern(pattern):
    ans = [[0 for i in range(len(pattern[0]))] for j in range(len(pattern))]
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            ans[i][len(pattern[0]) - 1 - j] = pattern[i][j]
    return ans

def reflectExcluded(pattern, row, col):
    ans = []
    for p in pattern:
        ans.append(reflectPoint(p, row, col))
    return ans

def reflectPoint(point, rows, cols):
    curPoint = (cols - 1 + point[1], rows - 1 + point[0])
    postPoint = (-curPoint[0], curPoint[1])
    postCorner = (0, rows - 1)
    return (postPoint[1] - postCorner[1], postPoint[0] - postCorner[0])




class Trie():
    def reset(self):
        self.g = [[-1 for i in range(maxS)] for j in range(numCnt)]
        self.f = [-1 for i in range(maxS)]
        self.output = [0 for i in range(numCnt)]

    def add_words(self, sList):
        states = 1
        for i in range(len(sList)):
            s = sList[i]
            curState = 0
            for c in s:
                if (self.g[curState][ord(c) - 97] == -1):
                    self.g[curState][ord(c) - 97] = states
                    states += 1
                curState = self.g[curState][ord(c) - 97]
            # showing that the i'th bit is 1 signifying that the i'th indexed element ends at curState
            self.output[curState] |= (1 << i)
    def preProcess(self):
        q = []

        for i in range(numCnt):
            if (self.g[0][i] == -1):
                self.g[0][i] = 0
            else:
                self.f[self.g[0][i]] = 0
                q.append(self.g[0][i])
        
        while (len(q) > 0):
            state = q[0]
            q.pop(0)

            for i in range(numCnt):
                if (self.g[state][i] != -1):
                    failure = self.f[state]
                    while (self.g[failure][i] == -1):
                        failure = self.f[failure]
                    failure = self.g[failure][i]
                    self.f[self.g[state][i]] = failure
                    self.output[self.g[state][i]] |= self.output[failure]
                    q.append(self.g[state][i])

    def getNextState(self, curState, transition):
        state = curState
        val = ord(transition) - 97
        while (self.g[state][val] == -1):
            state = self.f[state]
        return self.g[state][val]

    def search(self, s):
        curState = 0
        # only 1 pattern can possibly end at each state, so there is no need for subpatterns
        ans = [-1] * len(s)
        for j in range(len(s)):
            c = s[j]
            curState = self.getNextState(curState, c)
            if (self.output[curState] != 0):
                for i in range(numCnt):
                    if ((self.output[curState] & (1 << i)) > 0):
                        ans[j] = i
        return ans


def getPSTable(s):
    table = [0] * (len(s) + 1)
    i = 0
    j = 1
    while (j < len(s)):
        if (s[i] == s[j]):
            table[j + 1] = table[j] + 1
            i += 1
        else:
            i = 0
        j += 1
    
    return table

def getMatchIndices(s, psTable, m):
    targ = 0
    i = 0
    ans = []
    while (i < len(s)):
        while(targ < len(m) and i < len(s)):
            if (m[targ] == s[i]):
                targ+=1
                i+=1
            else:
                if (targ == 0):
                    i+=1
                break
        if (targ == len(m)):
            ans.append(i - 1)
        targ = psTable[targ]
    return ans

            

trie = Trie()

def updateNeighborGrid():
    global neighborGrid
    for i in range(1, len(neighborGrid) - 1):
        for j in range(1, len(neighborGrid[0]) - 1):
            if (grid[i][j] == -1):
                neighborGrid[i][j] = -1
            elif (grid[i][j] == -2):
                neighborGrid[i][j] = -2
            else:
                neighbors = getNeighbors(i, j)
                neighborGrid[i][j] = grid[i][j] - count(-2, neighbors)
            

def output(pattern):
    for j in range(len(pattern)):
        for k in range(len(pattern[0])):
            print(pattern[j][k], end = ' ')
        print()

# note that pattern and grid are already encoded
def searchGrid(grid, pattern):
    chain = ""
    map = {}
    index = 0
    newPatternString = ""
    for s in pattern:
        if (s in map):
            chain += str(map[s])
        else:
            map[s] = index
            index += 1
        newPatternString += chr(map.get(s) + 97)
    newPattern = []
    for key in map:
        newPattern.append(key)
    
    endings = [-1] * len(grid)
    trie.reset()
    trie.add_words(newPattern)
    trie.preProcess()

    for i in range(len(grid)):
        endings[i] = trie.search(grid[i])



    psTable = getPSTable(newPatternString)

    bottomRightCorners = []
    for i in range(len(endings[0])):
        line = ""
        for j in range(len(endings)):
            line += chr(endings[j][i] + 97)
        indices = getMatchIndices(line, psTable, newPatternString)
        for elem in indices:
            bottomRightCorners.append((elem, i))
    return bottomRightCorners

def checkExcluded(corner, excludedMines):
    for e in excludedMines:
        r = corner[0] + e[0]
        c = corner[1] + e[1]
        if (r < 1 or c < 1 or r >= len(neighborGrid) - 1 or c >= len(neighborGrid[0]) - 1 or neighborGrid[r][c] != -1):
            continue
        else:
            return False

    # for e in excluded:
    #     r = corner[0] + e[0]
    #     c = corner[1] + e[1]
    #     if (r < 1 or c < 1 or r >= len(neighborGrid) - 1 or c >= len(neighborGrid[0]) - 1 or (neighborGrid[r][c] != -1 and neighborGrid[r][c] != -2)):
    #         continue
    #     else:
    #         return False
    return True

# click pattern, 1 for click, 2 for mine, 0 for nothing
def processPattern(pattern, clickPattern, flagPattern, mineExcluded):
    newGrid = encodePattern(neighborGrid)
    newPattern = encodePattern(pattern)
    corners = searchGrid(newGrid, newPattern)
    for corner in corners:
        check = checkExcluded(corner, mineExcluded)
        if (not check):
            continue

        r = corner[0]
        c = corner[1]
        # subtracting 1 from the new value because the corner is 1 indexed, while click and flag are 0 indexed
        for i in range(len(flagPattern)):
            flag(r + flagPattern[i][0] - 1, c + flagPattern[i][1] - 1)
        for i in range(len(clickPattern)):
            click(r + clickPattern[i][0] - 1, c + clickPattern[i][1] - 1)




def solvePattern(pattern, clickPattern, flagPattern, minesExcluded):
    rowLen = len(pattern)
    colLen = len(pattern[0])
    patterns = []
    # excludedList = []
    mineExcludedList = []
    clickPatterns = []
    flagPatterns = []
    mineExcludedList.append(minesExcluded)
    # excludedList.append(excluded)
    clickPatterns.append(clickPattern)
    flagPatterns.append(flagPattern)
    patterns.append(pattern)
    r = len(patterns)
    c = len(patterns[0])
    for i in range(3):
        r = len(patterns[len(patterns) - 1])
        c = len(patterns[len(patterns) - 1][0])
        mineExcludedList.append(rotateExcluded(mineExcludedList[len(mineExcludedList) - 1], r, c))
        # excludedList.append(rotateExcluded(excludedList[len(excludedList) - 1], r, c))
        patterns.append(rotatePattern(patterns[len(patterns) - 1]))
        clickPatterns.append(rotateExcluded(clickPatterns[len(clickPatterns) - 1], rowLen, colLen))
        flagPatterns.append(rotateExcluded(flagPatterns[len(flagPatterns) - 1], rowLen, colLen))
        temp = rowLen
        rowLen = colLen
        colLen = temp
    rowLen = len(pattern)
    colLen = len(pattern[0])
    patterns.append(reflectPattern(patterns[0]))
    clickPatterns.append(reflectExcluded(clickPattern, rowLen, colLen))
    flagPatterns.append(reflectExcluded(flagPattern, rowLen, colLen))
    # excludedList.append(reflectExcluded(excludedList[0], rowLen, colLen)))
    mineExcludedList.append(reflectExcluded(mineExcludedList[0], r, c))
    for i in range(3):
        r = len(patterns[len(patterns) - 1])
        c = len(patterns[len(patterns) - 1][0])
        mineExcludedList.append(rotateExcluded(mineExcludedList[len(mineExcludedList) - 1], r, c))
        # excludedList.append(rotateExcluded(excludedList[len(excludedList) - 1], r, c))
        patterns.append(rotatePattern(patterns[len(patterns) - 1]))
        clickPatterns.append(rotateExcluded(clickPatterns[len(clickPatterns) - 1], rowLen, colLen))
        flagPatterns.append(rotateExcluded(flagPatterns[len(flagPatterns) - 1], rowLen, colLen))
        temp = rowLen
        rowLen = colLen
        colLen = temp

    for i in range(8):
            processPattern(patterns[i], clickPatterns[i], flagPatterns[i], mineExcludedList[i])


    

