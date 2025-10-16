def rotation(arr,steps):
    left=arr[steps:]
    right= arr[:steps]
    return left+right

arr=[1,2,3,4,5,6]
result= rotation(arr,3)

print(result)
.
.
.
.

