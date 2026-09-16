def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr=[20,5,27,47,55,67,75,88,90]
x=67
result=linearSearch(arr,x)

print("Searching element is present at index:", result)