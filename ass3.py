 #Ask the user to enter two integers and one float. Convert them all to floats and print their average.

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = float(input("Enter a float number:"))

#converting the integers to floats
num1=float(a)
num2=float(b)
num3=float(c)

average=(num1+num2+num3)/3

print("The average of the numbers is:", average)