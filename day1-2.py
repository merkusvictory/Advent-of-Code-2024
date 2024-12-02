rawinput = input()
list0 = rawinput.split()

list1 = []
list2 = []

odd = True

for i in list0:
    if odd == True:
        list1.append(i)
    if odd == False:
        list2.append(i)
    odd = not odd

list1.sort()
list2.sort()

similarity = 0

for i in list1:
    count = 0
    for f in list2:
        if int(i) == int(f):
            count+=1
    similarity += int(i) * count

print(similarity)