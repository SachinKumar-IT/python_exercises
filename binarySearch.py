def binarySearch(arr,x,i,j):
    while i<j:
        mid=i+(j-i)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:
            #return binarySearch(arr, x, mid+1,j)
            i= mid + 1
        else:
            #return binarySearch(arr,x,i,mid-j)
            j= mid - 1
    return -1

arr=[20,30,40,50,60,70,80,90]
x=80
i=0
j=len(arr)-1
result=binarySearch(arr,x,i,j)
print("Searching element is present at index:", result)