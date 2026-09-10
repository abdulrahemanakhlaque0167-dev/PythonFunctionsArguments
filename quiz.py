l=[ ("delhi"),
 ( "7"), 
 ( "mars"), 
 ( "10"),
 ( "python") 
 ]

point=0

answer=["What is the capital of India?",
   "Which planet is known as the Red Planet?",
   "How many days are there in a week?",
   "What is 5 + 5?",
   "Which language are we using to make this game?"
]

key=["If you have 3 apples and take away 2, how many apples do you have?","Which country gifted the Statue of Liberty to the United States?","What is the only even prime number?","A train travels 60 km in 1 hour. How far will it travel in 2 hours and 30 minutes?","Which is the smallest country in the world by area?"]

q=["Which is the largest ocean on Earth?","What is the square root of 144?","Which animal is known as the 'Ship of the Desert?'","How many bones does an adult human usually have?","Which planet has the most famous ring system?"]



d=input("enter the difficulty level, e for easy, m for medium and d for difficult: ")
if d=='e':
    print("welcome to the quiz game")
    print(answer[0])
    a1=input("enter the answer here: ")
    if a1=='delhi':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is delhi")
    print(answer[1])
    a2=input("enter the answer here: ")
    if a2=='mars':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is mars")
    print(answer[2])
    a3=input("enter the answer here: ")
    if a3=='7':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 7")
    print(answer[3])
    a4=input("enter the answer here: ")
    if a4=='10':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 10")
    print(answer[4])
    a5=input("enter the answer here: ")
    if a5=='python':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is python")
    print("your total point out of 5 are=",point)
elif d=='m':
    print(q[0])
    m1=input("enter the answer here: ")
    if m1=='pacific ocean':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is pacific ocean")
    print(q[1])
    m2=input("enter the answer here: ")
    if m2=='12':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 12")
    print(q[2])
    m3=input("enter the answer here: ")
    if m3=='camel':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is camel")
    print(q[3])
    m4=input("enter the answer here: ")
    if m4=='206':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 206")
    print(q[4])
    m5=input("enter the answer here: ")
    if m5=='saturn':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is saturn")
    print("your total points out of 5 are=",point)
elif d=='d':
    print(key[0])
    k1=input("enter the answer here: ")
    if k1=='2':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 2")
    print(key[1])
    k2=input("enter the answer here: ")
    if k2=='france':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is france")
    print(key[2])
    k3=input("enter the answer here: ")
    if k3=='2':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 2")
    print(key[3])
    k4=input("enter the answer here: ")
    if k4=='150':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is 150")
    print(key[4])
    k5=input("enter the answer here: ")
    if k5=='vatican city':
        print("correct")
        point+=1
    else:
        print("incorrect")
        print("the correct answer is vatican city")
    print("your total points out  of 5 are=",point)
else:
    print("the input is not among e,m or d")





'''
'''