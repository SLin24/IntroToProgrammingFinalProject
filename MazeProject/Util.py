import math
def getDirections(walls, w, h):
    # 0 = no direction, 1 = up, 2 = down, 3 = left, 4 = right
    directions = [[0 for x in range(w)] for y in range(h)] 
    visited = [[False for x in range(w)] for y in range(h)]


    queue = []
    # (r, c)
    queue.append((0, 0, 0))

    # Simple BFS Algorithm
    while (len(queue) != 0):
        first = queue[0]
        num = walls[first[0]][first[1]]
        queue.pop(0)
        
        if (visited[first[0]][first[1]]):
            continue
        visited[first[0]][first[1]] = True
        directions[first[0]][first[1]] = first[2]
        # if wall above is not present
        if (((1 << 3) & num) == 0):
            queue.append((first[0] - 1, first[1], 1))
        # if wall below is not present
        if (((1 << 2) & num) == 0):
            queue.append((first[0] + 1, first[1], 2))
        # if wall left is not present
        if (((1 << 1) & num) == 0):
            queue.append((first[0], first[1] - 1, 3))
        # if wall right is not present
        if ((1 & num) == 0):
            queue.append((first[0], first[1] + 1, 4))
        
    curPos = (h - 1, w - 1)
    listMoves = []
    while (curPos != (0, 0)):
        listMoves.append(directions[curPos[0]][curPos[1]])
        # if moved up to reach spot, move down
        if (directions[curPos[0]][curPos[1]] == 1):
            curPos = (curPos[0] + 1, curPos[1])
        # if moved down to reach spot, move up
        elif (directions[curPos[0]][curPos[1]] == 2):
            curPos = (curPos[0] - 1, curPos[1])
        # if moved left to reach spot, move right
        elif (directions[curPos[0]][curPos[1]] == 3):
            curPos = (curPos[0], curPos[1] + 1)
        # if moved right to reach spot, move left
        elif (directions[curPos[0]][curPos[1]] == 4):
            curPos = (curPos[0], curPos[1] - 1)
    listMoves.reverse()
    return listMoves

