def bubble_sort(Arr):
    n= len(Arr)
    for i in range(n):
        for j in range(n-i-1):
            if Arr[j]>Arr[j+1]:
                temp= Arr[j]
                Arr[j]= Arr[j+1]
                Arr[j+1] = temp
    return Arr

arr=[2,3,5,1,8,4]
print(bubble_sort(arr))