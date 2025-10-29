def find_kth_smallest_element(arr):
    smallest_ele=arr[0]
    for i in range(1,len(arr)):
        if arr[i] < smallest_ele:
            smallest_ele= arr[i]
    return smallest_ele
    
arr= [1,23,22,9,4,5,7,0]
res= find_kth_smallest_element(arr)
print(res)