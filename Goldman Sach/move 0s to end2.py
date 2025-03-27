def reframe(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i] == 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1

    return arr
arr=[2,0,4,0,5,0,7,8]
print(reframe(arr))

