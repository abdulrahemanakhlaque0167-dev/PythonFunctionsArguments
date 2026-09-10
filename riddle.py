
import random
x=["cat","sun","dog","banana","egg","apple","elephant","moon","car","fish"]

l=(random.choice(x))
if l=="cat":
    print("I say “meow” and I like to chase mice. What am I?")
elif l=="sun":
    print("I come out in the day and give you light. What am I?")
elif l=="dog":
    print("I say “woof” and I love to wag my tail. What am I?")
elif l=="banana":
    print("I am yellow and monkeys love to eat me. What am I?")
elif l=="egg":
    print("I am white outside and yellow inside. You can eat me for breakfast. What am I?")
elif l=="apple":
    print("I am red, round, and you can eat me. What am I?")
elif l=="elephant":
    print("I am very big and have a long trunk. What am I?")
elif l=="moon":
    print("I come out at night and shine in the sky. What am I?")
elif l=="car":
    print("I have four wheels and take you from one place to another. What am I?")
elif l=="fish":
    print("I live in water and I can swim. What am I?")
else:
    print()
    


while True:
    g=(input("enter a answer to guess: "))
    
    if g!=l:
        print("wrong answer")
    elif g==l:
        print("congratulation you won!")
        break



'''

'''