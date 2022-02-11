#calculating the largest number
a=float(input("Enter numer1:"))
b=float(input("Enter numer2:"))
c=float(input("Enter numer3:"))
if a>b and a>c:
  print("the largest number is a",a)
elif b>a and b>c:
  print("the largest number is b",b)
else:
  print("the largest number is c",c)