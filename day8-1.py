map = []

n = 50

for i in range(n):
    row = []
    rawinput = input()
    for char in rawinput:
        row.append(char)
    map.append(row)

nodeTypes = []
for row in map:
    for char in row:
        if char != '.':
            if char not in nodeTypes:
                nodeTypes.append(char)

print(nodeTypes)

def findingNodes(nodeType):
    list = []
    for rowNum in range(len(map)):
        for charNum in range(len(map[rowNum])):
            if map[rowNum][charNum] == nodeType:
                node = [charNum, rowNum]
                list.append(node)
    return list

#finding first one
antinodes = []
for nodeType in nodeTypes:
    nodeLocations = findingNodes(nodeType)
    for nodeLocationNum1 in range(len(nodeLocations)):
        for nodeLocationNum2 in range(nodeLocationNum1+1, len(nodeLocations)):
            Xdiff = nodeLocations[nodeLocationNum2][0] - nodeLocations[nodeLocationNum1][0]
            Ydiff = nodeLocations[nodeLocationNum2][1] - nodeLocations[nodeLocationNum1][1]
            antiX1 = nodeLocations[nodeLocationNum1][0] - Xdiff
            antiX2 = nodeLocations[nodeLocationNum2][0] + Xdiff
            antiY1 = nodeLocations[nodeLocationNum1][1] - Ydiff
            antiY2 = nodeLocations[nodeLocationNum2][1] + Ydiff
            if antiX1 < n and antiY1 < n and antiX1 >= 0 and antiY1 >= 0:
                antinode1 = [antiX1, antiY1]
                if antinode1 not in antinodes:
                    antinodes.append(antinode1)
            if antiX2 < n and antiY2 < n and antiX2 >= 0 and antiY2 >= 0:
                antinode2 = [antiX2, antiY2]
                if antinode2 not in antinodes:
                    antinodes.append(antinode2)

print(len(antinodes))