def twosum(arr,num):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == num:
                res.append([i,j])         
    return res

arr=[2,9,4,6]
num= 13
res= twosum(arr,num)
print(res)