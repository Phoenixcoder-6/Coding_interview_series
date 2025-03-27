def recheck(arr):
    res= [x for x in arr if x!=0]
    z_count= len(arr)-len(res)
    res.extend([0]* z_count)
    return res



arr=[1,2,3,0,9,0]
print(recheck(arr))