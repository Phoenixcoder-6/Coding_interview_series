def search(arr,target):
    low,high= 0,len(arr)-1
    mid= (low+high)//2

    if arr[mid] == target:
        return mid
    else:
        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            # Check if target lies in the left half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:
            # Check if target lies in the right half
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# Test the code
arr = [4, 5, 6, 7, 0, 1, 2]
target = 7
print(search(arr, target))
