def non_repeating_character(arr):
    lst={}
    for i in arr:
        if i in lst:
            lst[i]+=1
        else:
            lst[i]=1

    for i in arr:
        if lst[i]==1:
            return i
        
    return None

arr=[1,1,4,5,4,7]
result= non_repeating_character(arr)
print(result)