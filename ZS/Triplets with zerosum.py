def triplets(arr):
    arr.sort()
    n=len(arr)
    res=[]
    for i in range(n-2):
        left=i+1
        right= n-1
        while left < right:
            sum= arr[i] + arr[left] + arr[right]
            if sum==0:
                res.append((arr[i],arr[left],arr[right]))
                left +=1
                right -=1
            if sum <0:
                left +=1
            else:
                right -=1

    return res

arr=[0, -1, 2, -3, 1]
res= triplets(arr)
print(res)