def kth_smallestele(arr,k):
    n=len(arr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]= arr[min_ind],arr[i]

    return arr[k-1]

arr=[7,10,4,3,20,15]
k= 3
print(kth_smallestele(arr,k))