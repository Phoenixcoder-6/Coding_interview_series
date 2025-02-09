def linear_search(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return "Not Found"
        

arr=[2,3,4,1,8,6,7]
x= 4
res= linear_search(arr,x)
if res != "Not Found":
    print(f"{x} element is present at {res} position.")
else:
    print("Element not Found")