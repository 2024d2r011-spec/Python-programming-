text=input("Enter a string:")
vowels=0
consonents=0
digits=0
space=0
vowel_list="aeiouAEIOU"
for ch in text:
    if ch in vowel_list:
        vowel+=1
    elif ch.isalpha():
        consonents+=1
    elif ch.isdigits():
        digits+=1
    elif ch.isspace():
        space+=1

print("\nvowels:",vowels)
print("consonents:",consonents)
print("digits:",digits)
print("space:",space)
