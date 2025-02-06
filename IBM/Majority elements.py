def majority_elemets(arr):
    n=len(arr)
    freq={}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1

    for items,count in freq.items():
        if count > n/2:
            return items
    return -1


arr=[3,2,4,2,4,4,2,4,4]
print(majority_elemets(arr))


