def threesum(arr,num):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == num and arr[i] != arr[j] != arr[k]:
                    res.append([i,j,k])

    return res

nums = [-1, 0, 1, 2, -1, -4]
target=0

res= threesum(nums,target)

print(res)