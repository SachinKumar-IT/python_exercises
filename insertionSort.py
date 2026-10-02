def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


arr=[75,90,100,95,85,80]
result=insertionSort(arr)

print("Array after using Insertion Sort:", result)