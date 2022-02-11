#user login
username=str(input("Enter username:"))
print("username")
pwd=int(input("Enter password:"))
print("pasword")
login=["BSCIT-05-0233/2019",123]
if username in login and pwd in login:
  print("login successiful")
else:
  print("login failed")