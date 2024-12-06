map = []

n = 130
block = "#"

for i in range(n):
    row = []
    rawinput = input()
    for char in rawinput:
        row.append(char)
    map.append(row)


#finding guard initial
direction = "up"
for row in map:
    for position in row:
        if position == "^":
            x = row.index(position)
            y = map.index(row)
            break

#movement functions
def moveUp(y):
    y -= 1
    return y

def moveDown(y):
    y += 1
    return y

def moveLeft(x):
    x -= 1
    return x

def moveRight(x):
    x += 1
    return x


#checking for obstacles
def OGcheckFront(x,y,direction):
    if direction == "up":
        if [x,y-1] not in possibleBlocks:
            possibleBlocks.append([x,y-1])
        if y == 0:
            direction = "done"
        elif map[y-1][x] == block:
            direction ="right"
    elif direction =="down":
        if [x,y+1] not in possibleBlocks:
            possibleBlocks.append([x,y+1])
        if y == n-1:
            direction = "done"
        elif map[y+1][x] == block:
            direction = "left"
    elif direction == "left":
        if [x-1,y] not in possibleBlocks:
            possibleBlocks.append([x-1,y])
        if x == 0:
            direction = "done"
        elif map[y][x-1] == block:
            direction = "up"
    elif direction == "right":
        if [x+1,y] not in possibleBlocks:
            possibleBlocks.append([x+1,y])
        if x == n-1:
            direction = "done"
        elif map[y][x+1] == block:
            direction = "down"
    return direction

def checkFront(x,y,direction):
    if direction == "up":
        if y == 0:
            direction = "done"
        elif map[y-1][x] == block or (x == charNum and y-1 == rowNum):
            direction ="right"
    elif direction =="down":
        if y == n-1:
            direction = "done"
        elif map[y+1][x] == block or (x == charNum and y+1 == rowNum):
            direction = "left"
    elif direction == "left":
        if x == 0:
            direction = "done"
        elif map[y][x-1] == block or (x-1 == charNum and y == rowNum):
            direction = "up"
    elif direction == "right":
        if x == n-1:
            direction = "done"
        elif map[y][x+1] == block or (x+1 == charNum and y == rowNum):
            direction = "down"
    return direction

steppedOn = []
inf = 0

#looking at OGpath
possibleBlocks = []
def OGexecutePath(x,y,direction):
    while True:
        if direction == "up":
            y = moveUp(y)
        elif direction == "down":
            y = moveDown(y)
        elif direction == "left":
            x = moveLeft(x)
        elif direction == "right":
            x = moveRight(x)

        direction = OGcheckFront(x,y,direction)
        direction = OGcheckFront(x,y,direction)
        if direction == "done":
            break

OGexecutePath(x,y,direction)

#looping
def executePath(x,y,direction):
    loop = False
    steppedOn = []
    while True:
        if direction == "up":
            y = moveUp(y)
        elif direction == "down":
            y = moveDown(y)
        elif direction == "left":
            x = moveLeft(x)
        elif direction == "right":
            x = moveRight(x)

        #checking if stepped on before
        if [x,y,direction] not in steppedOn:
            steppedOn.append([x,y, direction])
        else:
            loop = True
            break

        direction = checkFront(x,y,direction)
        direction = checkFront(x,y,direction)
        if direction == "done":
            break
    return loop

possibleBlocks.pop()
print(possibleBlocks)
#looping through each map position
for i in possibleBlocks:
    rowNum = i[1]
    charNum = i[0]
    if executePath(x,y,direction) == True:
        inf += 1
        print(possibleBlocks.index(i), "/", len(possibleBlocks))

#printing out stuff
print(inf)