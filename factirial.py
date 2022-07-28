'''x = int(input("enter the factorial number : "))
fac = 1
while(x>0):
    fac = fac*x
    x = x-1
print("factorial : ",fac)'''

'''i=1
while i<=50:
    print(i,end=" ")
    i=i+2
print()

i=0
while i<=50:
    print(i,end=" ")
    i=i+2'''

'''x=int(input("enter the number: "))
n=0
n1=1
sum=0
if x<0:
    print("enter the positive number")
elif x==0:
    print("factorial 0 is 1")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n=n1
        n1=sum
        sum=n+n1'''

'''div=(lambda x,y:x/y)
print(div(10,5))'''


'''list1 =[2,6,8,9,7,5,4]
lam = lambda x:x%2==0
res=list(filter(lam,list1))
print(res)'''

list1=[3,5,7,9]
lam1 = lambda x:x*x
res =list(map(lam1,list1))
print(res)

