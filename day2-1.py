safes = 0
for i in range(0,1000):
    safe = True
    rawinput = input()
    list = rawinput.split()
    list = [int(x) for x in list]
    firstChange = list[1] - list[0]
    if firstChange > 0 and firstChange <= 3:
        for i in range(len(list)-1):
            change = list[i + 1] - list[i]
            if change <= 0 or change > 3:
                safe = False
    elif firstChange < 0 and firstChange >= -3:
        for i in range(len(list)-1):
            change = list[i + 1] - list[i]
            if change >= 0 or change < -3:
                safe = False
    else:
        safe = False
    if safe == True:
        safes += 1

print(safes)