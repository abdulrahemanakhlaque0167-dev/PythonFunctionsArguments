import random

print("welcome to the the penalty shooting game")
print("you get 1 point on every goal")
s=["l","r","c"]
goal=0
for i in range(5):
    h=random.choice(s)
    p=input("enter where you want to shoot l for left,r for right or c for centre: ")
    if h==p:
        print("it is not a goal it got saved by the goal keeper")
    elif h!=p:
        print("it is a goal! the goal keeper went in",h,"side")
        goal+=1
    else:
        print("you were said to write left,right or centre")
print("you got",goal,"points out of 5")
