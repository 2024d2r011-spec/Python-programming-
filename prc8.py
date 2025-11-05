num=int(input("Enter a number:"))
orig_num=num
sum=0
n=len(str(num))
while num>0:
    digit=num%10
    sum+=digit**n
    n//=10
if sum==orig_num:
    print("This is a palidrome number")
else:
    print("This is not a palindrome number")