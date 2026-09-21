def twoSum(arr,sum_value):
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l] + arr[r] == sum_value:
            return l,r
        elif arr[l] + arr[r] < sum_value:
            l+=1
        else:
            r-=1
    return -1

arr=[20,40,60,80,90,120,240]

sum_value=210

result=twoSum(arr,sum_value)
print("Sum pair indices are:", result)