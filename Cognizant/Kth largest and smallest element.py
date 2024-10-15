def elements(arr,k):
    arr.sort()
    largest= arr[-k]
    smallest= arr[k-1]
    return largest,smallest

arr=[2,3,6,1,24,9,256]
k=5
largest,smallest= elements(arr,5)
print(f"{k}th largest element is:",{largest})
print(f"{k}th smallest element is:",{smallest})
