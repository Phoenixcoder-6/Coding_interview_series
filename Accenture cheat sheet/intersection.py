def intersection(arr1,arr2):
    arr3= arr1+ arr2
    return arr3

arr1= [2,3,4,5,6]
arr2=[2,4,5,2,5]
arr3= intersection(arr1,arr2)

print(list(set(arr3)))