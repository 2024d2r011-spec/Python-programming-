string=input("Enter a string:")
string=string.lower()
if string==string[::-1]:
    print("This is a palindrome number")
else:
    print("This is not a palindrome number") 