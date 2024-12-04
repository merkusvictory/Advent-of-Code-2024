wordCount = 0
locationA = []

lines = []
for i in range(140):
    rawinput = input()
    lines.append(rawinput)

for lineNum in range(1,len(lines)-1):
    for letterNum in range(1,len(lines)-1):
        if lines[lineNum][letterNum] == "A":
            if (lines[lineNum-1][letterNum-1] == "M" and lines[lineNum+1][letterNum+1] == "S") or (lines[lineNum-1][letterNum-1] == "S" and lines[lineNum+1][letterNum+1] == "M"):
                if (lines[lineNum-1][letterNum+1] == "M" and lines[lineNum+1][letterNum-1] == "S") or (lines[lineNum-1][letterNum+1] == "S" and lines[lineNum+1][letterNum-1] == "M"):
                    wordCount += 1

print(wordCount)