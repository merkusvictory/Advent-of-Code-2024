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
def checkFront(x,y,direction):
    if direction == "up":
        if y == 0:
            direction = "done"
        elif map[y-1][x] == block:
            direction ="right"
    elif direction =="down":
        if y == n-1:
            direction = "done"
        elif map[y+1][x] == block:
            direction = "left"
    elif direction == "left":
        if x == 0:
            direction = "done"
        elif map[y][x-1] == block:
            direction = "up"
    elif direction == "right":
        if x == n-1:
            direction = "done"
        elif map[y][x+1] == block:
            direction = "down"
    return direction

steppedOn = []

#looping
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
    if [x,y] not in steppedOn:
        steppedOn.append([x,y])

    direction = checkFront(x,y,direction)
    direction = checkFront(x,y,direction)
    if direction == "done":
        break

#printing out stuff
for pair in steppedOn:
    map[pair[1]][pair[0]] = 'X'
for row in map:
    for char in row:
        print(char, end="")
    print("\n")
print(len(steppedOn))