from more_itertools import distinct_permutations
import itertools

n = 850

set = []
for i in range(n):
    row = []
    rawinput = input()
    rawinput = rawinput.split()
    for number in rawinput:
        if number[-1] == ":":
            number = number[:-1]
        row.append(int(number))
    set.append(row)


def operate(result, operation, num):
    if operation == "+":
        result += num
    if operation == "*":
        result *= num
    if operation == "||":
        result = int(str(result) + str(num))
    return result

valid = []
existingmidNums = []
for rowNum in range(len(set)):
    operation = "+"
    main = set[rowNum][0]
    set[rowNum].pop(0)
    midNums = 0

    midNums = len(set[rowNum]) - 1

    symbols = ["+", "*", "||"]
    perms = list(itertools.product(symbols,repeat = midNums))
    
    for perm in perms:
        result = set[rowNum][0]
        for opNum in range(len(perm)):
            result = operate(result, perm[opNum], set[rowNum][opNum+1])
            if result > main:
                break
        if result == main:
            valid.append(main)
            break
    
finSum = 0
for num in valid:
    finSum += num

print(finSum)
#result = operate(result, operation, set[rowNum][numNum])