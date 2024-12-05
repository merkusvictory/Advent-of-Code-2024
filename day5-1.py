rules = []
for i in range(1176):
    rawinput = input()
    rules.append(rawinput)

emptySpace = input()

orders = []
for i in range(203):
    rawinput = input()
    orders.append(rawinput)

pairs = []
for rule in rules:
    num1 = int(rule[:2])
    num2 = int(rule[3:])
    pairs.append([num1, num2])

sequences = []
for order in orders:
    sequence = []
    order = order.split(",")
    for num in order:
        sequence.append(int(num))
    sequences.append(sequence)

mids = []
for i in range(len(sequences)):
    valid = True
    sequencePairs = []
    for number1 in sequences[i]:
        for number2 in sequences[i]:
            sequencePairs.append([number1,number2])
    for pair in pairs:
        for seqPair in sequencePairs:
            if pair[0] in seqPair and pair[1] in seqPair:
                if sequences[i].index(pair[0]) > sequences[i].index(pair[1]):
                    valid = False
    print(valid)
    if valid == True:
        mids.append(sequences[i][len(sequences[i])//2])

sum = 0
for mid in mids:
    sum += mid
print(sum)