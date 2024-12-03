def digitDetector(i, rawinput):
    valid = True
    try:
        num1 = int(rawinput[i:i+3])
    except:
        try:
            num1 = int(rawinput[i:i+2])
        except:
            try:
                num1 = int(rawinput[i:i+1])
            except:
                valid = False
    if valid == True:
        return num1
    else:
        return 0

num1 = 0
num2 = 0
sum = 0
activate = True
for n in range(0,6):
    rawinput = input()
    for i in range(len(rawinput)):
        if rawinput[i:i+4] == "do()":
            activate = True
        if rawinput[i:i+7] == "don't()":
            activate = False
        if rawinput[i:i+4] == "mul(" and activate == True:
            num1 = digitDetector(i+4, rawinput)
            if num1 > 0:
                num2 = digitDetector(i+5+len(str(num1)), rawinput)
            if rawinput[i+4+len(str(num1))] == "," and rawinput[i+5+len(str(num1))+len(str(num2))] == ")":
                sum += num1*num2 
                print(rawinput[i:i+6+len(str(num1))+len(str(num2))])
print(sum)