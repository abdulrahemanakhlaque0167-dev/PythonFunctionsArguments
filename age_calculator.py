a=int(input("enter the year you were born: "))
h=2026-a
if a<=1900:
    print("were you really born before 1900")
elif a>=2026:
    print("how can you be born after 2026 ")
else:
    print("if you were born in the year",a,"your age is",h)