def plus_one(arr):
    num=''
    for i in range(len(arr)):
        num += str(arr[i])
    num = int(num)+1
    result =[]
    for d in str(num):
        result.append(int(d))
    return result
    
arr=[1,2,4]
res= plus_one(arr)
print(res)