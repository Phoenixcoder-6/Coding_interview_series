def LinearSearch_String(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i]== x:
            return i
    return -1

arr=['ashish','Uday','Anks']
x='Uday'
res= LinearSearch_String(arr,x)
if res != -1:
    print(f"{x} present at position {res+1}")
else:
    print("NA")