#Sum of first 1-100 prime numbers

num=int(input("Enter a number:"))
for i in range(num):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)