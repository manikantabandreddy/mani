'''list = [2,3,5,5,3,4,7,6]
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
list1.sort()
print(list1)'''

'''for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()'''

'''for i in range(6):
    for j in range(6-i):
        print("*",end="")
    print()'''

'''for i in range(6):
    for k in range(6-i):
        print(end=" ")
    for j in range(i+1):
        print("*",end= " ")
    print()'''


for i in range(6):
    for k in range(6+i):
        print(end=" ")
    for j in range(6-i):
        print("*",end= " ")
    print()



'''for i in range(1,6):
    for j in range(i+1):
        print(i+j,end=" ")
    print()'''
