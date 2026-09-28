def ternarySearch(arr,l,r,key):
    while l<=r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if arr[mid1]==key:
            return mid1
        elif arr[mid2]==key:
            return mid2
        elif key<arr[mid1]:
            return ternarySearch(arr,l,mid1-1,key)
        elif key>arr[mid2]:
            return ternarySearch(arr,mid2+1,r, key)
        else:
            return ternarySearch(arr,mid1-1,mid2-1,key)
    return -1


arr = [20,25,47,56,59,63,65,79,82]
key=79
l=0
r=len(arr)-1

result=ternarySearch(arr,l,r,key)
if result==-1:
    print("Element not found in the array")
else:
    print("Element found at index:", result)
