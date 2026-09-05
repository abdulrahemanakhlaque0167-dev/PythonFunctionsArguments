
f=int(input("enter the number for increaing lines: "))

for i in range(1,f+1):
    for j in range(i):
        print('*',end=' ')
    print()

g=int(input("enter the number for decreasing lines: "))
for i in range(g,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

h=int(input("enter the number for loop to run: "))
n=1
for i in range(1,h+1):
    for j in range(i):
        print(n,end=' ')
        n+=1
    print()