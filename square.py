import random 
import sys
sys.set_int_max_str_digits(43000)
e=int(input("enter a number to make it square,cube and table of the number: "))
sq=e*e
c=e*e*e
for i in range(1,11):
    print(e,"multiplied by",i,"is:",i*e)
print("square of number is=",sq)
print("cube of the number is=",c)
