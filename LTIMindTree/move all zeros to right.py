def organize(arr):
    zero=[]
    for i in arr:
        if i==0:
            zero.append(i)
            arr.remove(i)

    return arr+zero


arr=[23,45,34,1,9,0,8,0,3,2,0]
res= organize(arr)
print(res)
