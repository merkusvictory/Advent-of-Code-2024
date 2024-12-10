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

dotCount = 0

for char in newLine:
    if char == '.':
        dotCount += 1

max = len(newLine) -1
min = 0
for ascendingCharNum in range(min, len(newLine)-dotCount):
    if newLine[ascendingCharNum] == '.':
        for descendingCharNum in range(max, -1, -1):
            if newLine[descendingCharNum] != '.':
                newLine[ascendingCharNum] = newLine[descendingCharNum]
                newLine[descendingCharNum] = '.'
                max = descendingCharNum
                min = ascendingCharNum
                break
    print(ascendingCharNum, "/", len(newLine)-dotCount)

sum = 0
for i in range(len(newLine) - dotCount):
    sum += i*(newLine[i])
# separated = []
# for i in range(len(newLine) - dotCount):
#     newLine[i] = str(newLine[i])
#     for f in newLine[i]:
#         separated.append(f)

# for i in range(len(separated)):
#     sum += i*int(separated[i])
# print(separated)
print(newLine[:-(dotCount)])
print(sum)