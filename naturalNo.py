#Sum of first n natural numbers using while and for loop

n=int(input("Enter a number:"))
sum=0

# while count<=n:
#     sum+=count
#     count+=1

# print(f"Sum of First {n} natural numbers is {sum}")

for i in range(n+1):
    sum+=i

print(f"Sum of first {n} natural numbers is {sum}")