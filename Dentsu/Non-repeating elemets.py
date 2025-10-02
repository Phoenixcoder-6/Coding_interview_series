def unique(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    res=[]
    for items,count in freq.items():
        if count ==1:
            res.append(items)
    
    return res

arr=[1,2,3,2,1,5]
res= unique(arr)
print(res)
