def check(arr):
    front=[]
    middle=[]
    end=[]
    for i in arr:
        if i==0:
            front.append(i)
        elif i==1:
            middle.append(i)
        else:
            end.append(i)

    return front+middle+end


arr=[1,2,0,0,1,1,2,0]
res= check(arr)
print(res)