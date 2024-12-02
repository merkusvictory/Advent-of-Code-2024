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
dist = 0

list1.sort()
list2.sort()
print(len(list1))
print(len(list2))

for i in range(len(list1)):
    dist += abs(int(list1[i]) - int(list2[i]))

print(dist)