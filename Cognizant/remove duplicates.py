def remove_duplicates(arr):
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)

    return lst

arr=[1,2,3,3,4,5,6,6]
result= remove_duplicates(arr)
print(result)