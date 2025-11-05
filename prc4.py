n=int(input("Enter a number in terms:"))
a,b=0,1
print("\nfibonnaci series:")
if n<=0:
    print("Enter a positive number.")
elif n==1:
    print(a)
else:
    print(a,b,end="")
    for i in range(2,n):
     c=a+b
     print(c,end="")
     a=b
     b=c

