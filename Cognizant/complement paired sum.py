def find_pairs(arr,target_sum):
    pairs=[]
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target_sum:
                pairs.append((arr[i],arr[j]))

    return pairs
    

arr=[1,2,4,5,7,8]
target_sum=7
result= find_pairs(arr,target_sum)
print(result)
