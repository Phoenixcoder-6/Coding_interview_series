def productarr(arr):
    result=[1]* len(arr)
    prefix=1
    for i in range(len(arr)):
        result[i] =prefix
        prefix *= arr[i]
    suffix=1
    for i in range(len(arr)-1,-1,-1):
        result[i]*= suffix
        suffix *= arr[i]


    return result

arr=[1,2,3,4]
res= productarr(arr)
print(res)