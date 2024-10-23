def longest_subsequence(arr):
    n=len(arr)
    start=arr[0]
    lst=[start]
    j=1
    while j<n:
        if arr[j]>start:
            lst.append(arr[j])
            start=arr[j]
        else:
            j+=1
    return lst

arr = [10, 22, 9, 33, 21, 50, 41, 60]
result = longest_subsequence(arr)
print("Length of longest increasing subsequence is:", result)

