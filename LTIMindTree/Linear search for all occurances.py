def linear_search_Occurances(arr,x):
    n= len(arr)
    indices=[]
    for i in range(n):
        if arr[i] == x:
            indices.append(i)
        
    return indices if indices else -1


arr=[1,2,4,3,5,2,6,2,0]
x=2
res= linear_search_Occurances(arr,x)
if res != -1:
    print(f"{x} present at {res} positions.")
else:
    print("Element not present.")
