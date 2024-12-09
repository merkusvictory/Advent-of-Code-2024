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

antinodes = []
singleNodes = []
for nodeType in nodeTypes:
    nodeLocations = findingNodes(nodeType)
    if len(nodeLocations) == 1:
        singleNodes.append(nodeType)
    for nodeLocationNum1 in range(len(nodeLocations)):
        for nodeLocationNum2 in range(nodeLocationNum1+1, len(nodeLocations)):
            Xdiff = nodeLocations[nodeLocationNum2][0] - nodeLocations[nodeLocationNum1][0]
            Ydiff = nodeLocations[nodeLocationNum2][1] - nodeLocations[nodeLocationNum1][1]
            antiX1 = nodeLocations[nodeLocationNum1][0] - Xdiff
            antiY1 = nodeLocations[nodeLocationNum1][1] - Ydiff
            antiX2 = nodeLocations[nodeLocationNum2][0] + Xdiff
            antiY2 = nodeLocations[nodeLocationNum2][1] + Ydiff
            antiX3 = nodeLocations[nodeLocationNum1][0] + Xdiff
            antiY3 = nodeLocations[nodeLocationNum1][1] + Ydiff
            while antiX1 < n and antiY1 < n and antiX1 >= 0 and antiY1 >= 0:
                antinode1 = [antiX1, antiY1]
                if antinode1 not in antinodes:
                    antinodes.append(antinode1)
                antiX1 = antiX1 - Xdiff
                antiY1 = antiY1 - Ydiff
            while antiX2 < n and antiY2 < n and antiX2 >= 0 and antiY2 >= 0:
                antinode2 = [antiX2, antiY2]
                if antinode2 not in antinodes:
                    antinodes.append(antinode2)
                antiX2 = antiX2 + Xdiff
                antiY2 = antiY2 + Ydiff
            while antiX3 < n and antiY3 < n and antiX3 >= 0 and antiY3 >= 0:
                antinode3 = [antiX3, antiY3]
                if antinode3 not in antinodes:
                    antinodes.append(antinode3)
                antiX3 = antiX3 + Xdiff
                antiY3 = antiY3 + Ydiff

for rowNum in range(len(map)):
    for charNum in range(len(map[rowNum])):
        if map[rowNum][charNum] != ".":
            antinode = [charNum, rowNum]
            if (antinode not in antinodes) and (map[rowNum][charNum] not in singleNodes):
                antinodes.append(antinode)

print(len(antinodes))