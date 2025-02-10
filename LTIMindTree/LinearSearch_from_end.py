def linear_end(arr,x):
    n= len(arr)
    for i in range(n-1,-1,-1):
        if arr[i]==x:
            return i
    return -1

arr=[2,3,5,1,6,8]
x=6
res= linear_end(arr,x)

if res != -1:
    print(res)
else:
    print("NA")