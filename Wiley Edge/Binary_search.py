def binary_search(arr,target):
    low=0
    high= len(arr)-1

    while low <= high:
        mid= (low+high) //2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid+1 
        else:
            high = mid-1
    return -1

my_list=[1,4,3,2,7,8]
my_list.sort()
target_value = 4
result = binary_search(my_list,target_value)
print(result)