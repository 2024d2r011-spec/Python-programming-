sub1=float(input("Enter marks of subject1:" ))
sub2=float(input("Enter marks of subject2:" ))
sub3=float(input("Enter marks of subject3:" ))
sub4=float(input("Enter marks of subject4:" ))
sub5=float(input("Enter marks of subject5:" ))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("/nTotal marks obtained:",total)
print("percentage:",percentage,"%")
if percentage>=90:
    Grade="A"
elif percentage>=80:
    Grade="B"
elif percentage>=70:
    Grade="C"
elif percentage>=60:
    Grade="D"
else:
    print("Fail")    
print("Grade:",Grade)            
