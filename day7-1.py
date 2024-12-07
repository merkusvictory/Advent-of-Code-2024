from more_itertools import distinct_permutations

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
    if operation == "add":
        result += num
    if operation == "multiply":
        result *= num
    return result

valid = []
for rowNum in range(len(set)):
    operation = "add"
    main = set[rowNum][0]
    set[rowNum].pop(0)
    midNums = 0

    midNums = len(set[rowNum]) - 1

    operationsList = []
    operationsRow = []
    for i in range(midNums):
        operationsRow.append("add")
    for i in range(midNums):
        operationsRow.append("multiply")
    perms = [p for p in distinct_permutations(operationsRow)]
    permss = []
    # for perm in perms:
    #     ii = []
    #     for i in perm:
    #         ii.append(i)
    #     permss.append(ii)
    for perm in perms:
        if perm[:midNums] not in operationsList:
            operationsList.append(perm[:midNums])

    for i in range(len(operationsList)):
        result = set[rowNum][0]
        for opNum in range(len(operationsList[i])):
            result = operate(result, operationsList[i][opNum], set[rowNum][opNum+1])
        if result == main:
            valid.append(main)
            break
    print(rowNum, "/", len(set))
    
finSum = 0
for num in valid:
    finSum += num

print(finSum)
#result = operate(result, operation, set[rowNum][numNum])