def find_kth_element(arr,k):
    arr.sort()
    return arr[k-1]

arr=[4,5,2,1,8,5,6,8]
k=2
res=find_kth_element(arr,k)
print(res)