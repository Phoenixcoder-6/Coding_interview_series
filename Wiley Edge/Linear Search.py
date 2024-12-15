def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        
    return None
        
arr=[2,3,7,78,9,45]
target= 45
res= linear_search(arr,target)
print("The element is present at position:", res)