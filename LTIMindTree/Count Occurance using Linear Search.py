def Count_Occurance(arr,x):
    n= len(arr)
    count=0
    for i in range(n):
        if arr[i] == x:
            count+=1
    return count if count else -1


arr=[2,3,4,2,6,2,3,4,2]
x=2
res= Count_Occurance(arr,x)

if res != -1:
    print(f"{x} element present {res} times.")
else:
    print("Element not present.")
