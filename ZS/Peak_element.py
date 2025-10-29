def peak_ele(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i]> arr[i+1]:
            return (arr[i],i)
        
    return None

arr=[1, 2, 4, 5, 7, 8, 3]
res= peak_ele(arr)
print(res)
        
