import random
f=random.randint(1,100)
point=100
print("welcome to the number guessing game")
print("you have ten tries to guess the number")
print("each wrong decreases 10 point from total 100 points")
print("try to guess it as early as possible")
for i in range(10):
    g=int(input("enter the guess: "))
    if g==f:
        print("you won in",i,"attemps")
        print("your point is=",point)
        break
    elif g>=f:
        print("your guess is high, go lower")
        point-=10
    else:
        print("your guess is low, go higher")
        point-=10
else:
    print("you lost")
    print("you got 0 points")