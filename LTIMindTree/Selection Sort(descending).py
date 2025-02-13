def selection_sort_desc(arr):
    n=len(arr)
    for i in range(n):
        max_ind=i
        for j in range(i+1,n):
            if arr[j]>arr[max_ind]:
                max_ind=j
        arr[i], arr[max_ind] = arr[max_ind], arr[i]

    return arr


arr=[5,3,7,2,1]
print(selection_sort_desc(arr))