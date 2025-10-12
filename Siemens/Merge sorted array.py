def merge_arrays(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1
nums1=[1,2,3,4,5]
nums2= [6,3,2]
res= merge_arrays(nums1,nums2)
print("Merged array:", res)