def Selection_sort(arr):
    n= len(arr)
    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if arr[j]< arr[min_indx]:
                min_indx=j
        arr[i],arr[min_indx]= arr[min_indx],arr[i]

    return arr


arr=[3,5,4,7,2,9,10,8]
print(Selection_sort(arr))
