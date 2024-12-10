word = "0123456789"
wordCount = 0

lines = []
for i in range(55):
    rawinput = input()
    lines.append(rawinput)

def letterScanner(lineList, lineNum, letterNum, startLetter, endLetter):
    valid = []
    if lineList[lineNum][letterNum] == startLetter:
        #print("found a match on",lineNum,letterNum, startLetter)
        if letterNum != len(lines)-1:
            if lineList[lineNum][letterNum+1] == endLetter:
                valid.append([lineNum, letterNum+1])
        if lineNum != len(lines)-1:
            if lineList[lineNum+1][letterNum] == endLetter:
                valid.append([lineNum+1, letterNum])
        if letterNum != 0:
            if lineList[lineNum][letterNum-1] == endLetter:
                valid.append([lineNum, letterNum-1])
        if lineNum != 0:
            if lineList[lineNum-1][letterNum] == endLetter:
                valid.append([lineNum-1, letterNum])
    return valid


#finding first letter
fletters = []
for rowNum in range(len(lines)):
    for charNum in range(len(lines[rowNum])):
        if lines[rowNum][charNum] == word[0]:
            fletters.append([rowNum, charNum])

total = 0
for fletter in fletters:
    valid = []
    valid.append(fletter)
    score = 0

    for letter in range(len(word)-1):
        n = len(valid)
        for pair in range(n):
            coords = letterScanner(lines, valid[pair][0], valid[pair][1], word[letter], word[letter+1])
            for coord in coords:
                valid.append(coord)
        del valid[:n]
    
    final = []
    for i in valid:
        if i not in final:
            final.append(i)
    
    for i in final:
        score+=1
    
    total += score
    print(fletters.index(fletter),"/",len(fletters))
    
#     print(valid)
#     print(score)
print(total)