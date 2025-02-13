def string_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_idx]):
                min_idx = j
        # Swap the elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = ["apple", "banana", "kiwi", "pear"]
print(string_sort(arr))
