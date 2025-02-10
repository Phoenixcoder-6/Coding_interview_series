def bubble(arr):
    n= len(arr)
    count=0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                count+=1
    return arr,count
arr=[64, 25, 12, 22, 11]
print(arr)
print(bubble(arr))