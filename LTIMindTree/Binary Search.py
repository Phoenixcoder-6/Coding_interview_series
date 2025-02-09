def Binary_search(arr,x):
    low=0
    high= len(arr)-1
    while low<=high:
        mid=  low+ (high-low)//2

        if arr[mid]== x:
            return mid
        elif arr[mid]<x:
            low= mid+1
        else:
            high = mid-1

    return -1

arr=[1,2,4,5,6,7,89]
x=5
res= Binary_search(arr,x)

print("Original array is:",arr)

if res != -1:
    print(f"{x} element present at {res} position.")
else:
    print("Element not present")