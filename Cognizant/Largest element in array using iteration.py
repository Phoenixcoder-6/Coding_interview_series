def largest_element(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest= arr[i]
        
    return largest

arr=[23,45,67,900]
result= largest_element(arr)
print(result)
        
