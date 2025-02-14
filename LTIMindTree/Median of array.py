def median(arr1,arr2):
    arr= sorted(arr1+arr2)
    n= len(arr)
    if n%2 !=0:
        return arr[n//2]
    else:
        return (arr[n//2]+ arr[(n-1)//2])/2
    

arr1=[1,2,3,4]
arr2=[8,6]
res= median(arr1,arr2)
print(res)