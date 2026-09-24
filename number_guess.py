import random
print("welcome to the number guessing game")
print("try to guess it as early as possible")
h=int(input("enter the the number from 1 to anything you want in which the number will generate that you have to guess: "))
q=int(input("enter the number of  attemps you want: "))
f=random.randint(1,h)


for i in range(q):
    g=int(input("enter the guess: "))
    if g==f:
        print("congratulations you won")
        print("you won in",i,"attemps")
        break
    elif g>=f:
        print("your guess is high, go lower")
    else:
        print("your guess is low, go higher")
else:
    print("you lost")
    print("you got 0 points")
    