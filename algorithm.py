English=int(input("Enter Eng:"))
Mathematics=int(input("Enter Maths:"))
Kiswahili=int(input("Enter Kisw:"))
Chemistry=int(input("Enter Chem:"))
Physics=int(input("Enter Phy:"))
Average=((English+Mathematics+Kiswahili+Chemistry+Physics)/5)
print(Average)
if Average>=70 and Average <=100:
    print("Grade A")
elif Average>=60 and Average<=69:
    print("Grade B")
elif Average>=50 and Average<59:
    print("Grade C")
elif Average>=40 and Average<=49:
    print("Grade D")
else:
    print("Fail")

