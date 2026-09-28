a=int(input("enter the year you were born: "))
h=2026-a
if a<=1909:
    print("were you realy born before the oldest person living on earth?")
    print("although your age is",h)
elif a>2026:
    print("how can you be born after 2026 ")
elif a==2026 or a==2025 or a==2024:
    print("if you were born in",a,"it mean you just got born and started using python!!")
    print("although your age is",h)
else:
    print("if you were born in the year",a,"your age is",h)
    