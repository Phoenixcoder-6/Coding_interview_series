def dutch(arr):
    front=[]
    middle=[]
    last=[]
    for i in arr:
        if i==0:
            front.append(i)
        elif i==1:
            middle.append(i)
        else:
            last.append(i)

    return front+middle+last

arr=[1,0,0,2,2,0,1,2,0,1]
result= dutch(arr)
print(result)