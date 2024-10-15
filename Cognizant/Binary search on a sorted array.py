def binary_search(arr,item):
    n=len(arr)
    lower_bound= 0
    upper_bound= n-1
    while lower_bound<= upper_bound:
        mid= (lower_bound+upper_bound)//2
        if item==arr[mid]:
            return mid
        elif item<arr[mid]:
            upper_bound=mid-1
        else:
            lower_bound=mid+1

arr=[1,2,4,5,6,7]
result= binary_search(arr,5)
print("Item present at index:",result)