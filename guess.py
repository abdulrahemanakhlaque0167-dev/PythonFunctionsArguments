
import random
n=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x=[]

l=(random.choice(n))
while True:
    print("your guesses are",x)
    g=(input("enter a alphabet to guess: "))
    x.append(g)
    if g!=l:
        print("wrong")
    elif g==l:
        print("congratulation you won!")
        break