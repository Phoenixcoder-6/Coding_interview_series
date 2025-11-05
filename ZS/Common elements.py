def find_common(arr1,arr2,arr3):
    return list(set(arr1) & set(arr2) & set(arr3))

arr1=[2,3,5,6,7]
arr2=[4,5,6,7,8]
arr3=[5,6,10,12,56]
res= find_common(arr1,arr2,arr3)

print(res)
.
