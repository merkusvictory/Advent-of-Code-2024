rawinput = input()
rawinput += input()
newLine = []
count = 0

for i in range(len(rawinput)):
    if i % 2 == 0:
        newLine += [count] * int(rawinput[i])
        count += 1
    else:
        newLine += ['.'] * int(rawinput[i])



max = len(newLine) -1
min = 0
scannedIDs = []
for descendingCharNum in range(max, -1, -1):
    if newLine[descendingCharNum] != '.' and newLine[descendingCharNum] not in scannedIDs:
        scannedIDs.append(newLine[descendingCharNum])
        currentID = newLine[descendingCharNum]
        IDwidth = 1
        while newLine[descendingCharNum - IDwidth] == currentID:
            IDwidth += 1
        for ascendingCharNum in range(min, max):
            if newLine[ascendingCharNum] == '.':
                dotWidth = 1
                while newLine[ascendingCharNum + dotWidth] == ".":
                    dotWidth += 1

                if IDwidth <= dotWidth and ascendingCharNum < descendingCharNum:
                    newLine[ascendingCharNum:ascendingCharNum + IDwidth] = newLine[descendingCharNum - IDwidth+1:descendingCharNum+1]
                    newLine[descendingCharNum - IDwidth+1:descendingCharNum+1] = ['.'] * IDwidth
                    max = descendingCharNum - IDwidth
                    break
                max = descendingCharNum - IDwidth
    if max == -1:
        break
print(len(newLine))
sum = 0
for i in range(len(newLine)):
    if newLine[i] != ".":
        sum += i*(newLine[i])

print(sum)