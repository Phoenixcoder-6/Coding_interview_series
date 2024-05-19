def largest_subarray_with_largest_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = end = s = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return arr[start:end + 1], max_so_far

# Example usage
array = list(map(int, input("Enter the array elements separated by commas: ").split(',')))
subarray, largest_sum = largest_subarray_with_largest_sum(array)
print("The largest subarray with the largest sum is:", subarray)
print("The largest sum is:", largest_sum)
