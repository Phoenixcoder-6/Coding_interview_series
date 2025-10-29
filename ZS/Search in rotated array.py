def search_number(arr,k):
    for i in range(len(arr)):
        if arr[i] ==k:
            return i
    return -1


arr=[5, 6, 7, 8, 9, 10, 1, 2, 3]
k=3
res= search_number(arr,k)
print(res)
