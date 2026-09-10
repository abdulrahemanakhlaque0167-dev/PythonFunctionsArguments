import random
f=[
    "apple", "banana", "mango", "orange", "grapes",
    "pineapple", "watermelon", "papaya", "guava", "strawberry",
    "cherry", "peach", "pear", "melon", "kiwi",
    "coconut", "lemon", "lime", "pomegranate", "fig",
    "date", "avocado", "jackfruit", "lychee", "raspberry",
    "blueberry", "blackberry", "cantaloupe", "muskmelon", "tangerine"
]
l=random.choice(f)
k=100
for i in range(5):
    g=input("enter your guess: ")
    if g==l:
        print("you won")
        print("your points are",k-20*i)
        break
    elif g!=l:
        print("your answer is wrong")
        if i==0:
            h1=len(l)
            print("your first hint is")
            print("the fruit is",h1,"letters long")
        elif i==1:
            h2=l[0]
            print("your second hint is")
            print("the fruit starts with",h2)
        elif i==2:
            h3=l[0]
            for j in range(len(l)-1):
                h3=h3+'*'
            print("the third hint is")
            print("the fruit is like",h3)
        elif i==3:
            h4=l[0]
            for j in range(len(l)-2):
                h4=h4+'*'
            print("the fruit ends with",l[-1])
            print("the name is like",h4+l[-1])
        else:
            print("you lost")
            print("the fruit was",l)
            print("you got 0 points")
    else:
        pass


    
    
        
