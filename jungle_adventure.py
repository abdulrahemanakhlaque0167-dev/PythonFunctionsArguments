print("you came into jungle for fun")
print("but!!")
print("you got stuck and cannot find the way out")
print("you see two paths where do you want to go")

x=input("enter left or right: ")
if x=='left':
    print("you turned left and found a giant snake")
    print("do you want to go or attack  him")
    i=input("enter go or attack: ")
    if i=='go':
        print("you went safely and made your way out")
        print("now you see two gates one is safe and one is deadly")
        v=input("enter one or two: ")
        if v=='one':
            print("you chose the deadly path")
            print("there were tigers who attacked you")
            print("you died")
        elif v=='two':
            print("you chose the safe door")
            print("congratulations, you made your way out safely")
        else:
            print("something went wrong")
    elif i=='attack':
        print("you tried to attack the snake and it got aggresive and killed you")
    else:
        print("something went wrong")
elif x=='right':
    print("you found a lion sleeping")
    print("what are you going to do")
    print("do you want to go or do you want to attack")
    a=input("enter go or attack: ")
    if a=='go':
        print("you went pass by without him noticing")
        print("but as you turned back he attacked")
        print("you died because you couldnt fight ")
    elif a=='attack':
        print("you attacked him and he died")
        print("now you see two more ways")
        print("one of them is safe and other one is deadly")
        s=input("enter one or two: ")
        if s=='one':
            print("you chose the deadly door!")
            print("a monster is chasing you")
            u=input("enter f to fight back or h to hide: ")
            if u=='f':
                print("you tried to fight back and died")
            elif u=='h':
                print("you tried to hide but he found you")
                print("he picked you up and hit you on the head")
                print("you died")
            else:
                print("something went wrong")
        elif s=='two':
            print("you chose the safe door")
            print("you made your way out")
        else:
            print("something went wrong")
    else:
        print("something went wrong")
else:
    print("something went wrong")



