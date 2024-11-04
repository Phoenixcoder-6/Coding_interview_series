def reverse(A,start,end):
    while start<end:
        A[start],A[end]= A[end],A[start]
        start+=1
        end-=1
    return A

arr=[2,3,4,5]
res= reverse(arr,0,3)
print(res)