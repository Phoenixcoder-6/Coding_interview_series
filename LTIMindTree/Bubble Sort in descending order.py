def bubble_desc(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr


arr=[4,5,7,2,9,3,6]
print(bubble_desc(arr))