def first_occurance(arr,x):
    n= len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1
    

arr=[2,3,3,1,4,2,4,2]
x=3

res=first_occurance(arr,x)
print(res)