#calculate the sum of number using user input and if user enter 0 then quit.
total=0
number=int(input("enter a number(0 or to quit):"))
while number!=0:
      total+=number
      number=int(input("enter a number(0 or to quit):"))
print("total is", total)


