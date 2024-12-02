safes = 0
redos = []

def safeChecker (list):
    safe = True
    firstChange = list[1] - list[0]
    if firstChange > 0 and firstChange <= 3:
        for i in range(len(list)-1):
            change = list[i + 1] - list[i]
            if change <= 0 or change > 3:
                safe = False
                break
    elif firstChange < 0 and firstChange >= -3:
        for i in range(len(list)-1):
            change = list[i + 1] - list[i]
            if change >= 0 or change < -3:
                safe = False
                break
    else:
        safe = False
    return safe

for i in range(0,1000):
    rawinput = input()
    list = rawinput.split()
    list = [int(x) for x in list]
    if safeChecker(list) == True:
        safes+=1
    else:
        redos.append(list)

for list in redos:
    for i in range(len(list)):
        print(list[:i]+list[i+1:])
        if safeChecker(list[:i]+list[i+1:]) == True:
            safes+=1
            break
print(safes)