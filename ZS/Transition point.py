def transition_point(arr):
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            return i+1
    return -1
        
arr=[0,0,0,1,1,1,1]
res= transition_point(arr)
print(res)