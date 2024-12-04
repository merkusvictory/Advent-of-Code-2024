word = "XMAS"
wordCount = 0

lines = []
for i in range(140):
    rawinput = input()
    lines.append(rawinput)

def letterScanner(lineList, lineNum, letterNum, startLetter, endLetter):
    valid = []
    if lineList[lineNum][letterNum] == startLetter:
        print("found a match on",lineNum,letterNum, startLetter)
        if letterNum != len(lines)-1:
            if lineList[lineNum][letterNum+1] == endLetter:
                valid.append("right")
        if letterNum != len(lines)-1 and lineNum != 0:
            if lineList[lineNum-1][letterNum+1] == endLetter:
                valid.append("up right")
        if lineNum != len(lines)-1:
            if lineList[lineNum+1][letterNum] == endLetter:
                valid.append("down")
        if lineNum != len(lines)-1 and letterNum != 0:
            if lineList[lineNum+1][letterNum-1] == endLetter:
                valid.append("down left")
        if lineNum != len(lines)-1 and letterNum != len(lines)-1:
            if lineList[lineNum+1][letterNum+1] == endLetter:
                valid.append("down right")
        if letterNum != 0:
            if lineList[lineNum][letterNum-1] == endLetter:
                valid.append("left")
        if letterNum != 0 and lineNum != 0:
            if lineList[lineNum-1][letterNum-1] == endLetter:
                valid.append("up left")
        if lineNum != 0:
            if lineList[lineNum-1][letterNum] == endLetter:
                valid.append("up")
    return valid

def continuedScanner(lineList, path, startLetter, endLetter):
    if path == "right":
        if path in letterScanner(lineList, lineNum, letterNum+i, startLetter, endLetter):
            return True
    elif path == "left":
        if path in letterScanner(lineList, lineNum, letterNum-i, startLetter, endLetter):
            return True
    elif path == "down left":
        if path in letterScanner(lineList, lineNum+i, letterNum-i, startLetter, endLetter):
            return True
    elif path == "down":
        if path in letterScanner(lineList, lineNum+i, letterNum, startLetter, endLetter):
            return True
    elif path == "down right":
        if path in letterScanner(lineList, lineNum+i, letterNum+i, startLetter, endLetter):
            return True
    elif path == "up left":
        if path in letterScanner(lineList, lineNum-i, letterNum-i, startLetter, endLetter):
            return True
    elif path == "up":
        if path in letterScanner(lineList, lineNum-i, letterNum, startLetter, endLetter):
            return True
    elif path == "up right":
        if path in letterScanner(lineList, lineNum-i, letterNum+i, startLetter, endLetter):
            return True
    return False


for lineNum in range(len(lines)):
    for letterNum in range(len(lines)):
        paths = letterScanner(lines, lineNum, letterNum, word[0], word[1])
        for path in paths:
            found = True
            for i in range(1, len(word)-1):
                if continuedScanner(lines, path, word[i], word[i+1]) == False:
                     found = False
                     print("wrong")
                     break
                else:
                    print("correct path for", path)
            if found == True:
                wordCount += 1
                print("Word Count:", wordCount)

print(wordCount)