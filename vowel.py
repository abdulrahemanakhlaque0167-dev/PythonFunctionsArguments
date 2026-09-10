vowel=[]
consonent=[]
for i in range(10):
    v=input("enter a alphabet: ")

    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        print("it is a vowel!")
        vowel.append(v)
    elif v=='A' or v=='E' or v=='I' or v=='O' or v=='U':
        print("it is a vowel!")
        vowel.append(v)    
    else:
        print("it is a consonent!")
        consonent.append(v)

print("vowels are=",vowel)
print("consonents are=",consonent)
