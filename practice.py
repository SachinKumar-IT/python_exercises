# age=int(input("Enter your age:"))

# if age<=13:
#     print("You are a child.")

# elif age>13 and age<18:
#     print("You are a teenager.")

# else:
#     print("You are an adult.")

username =input("Enter your username:")
password=input("Enter your password:")

if username=="admin" and password=="pass":
    print("Login successful.")

elif username!="admin":
    print("Wrong username.")

else:
    print("Wrong Password.")