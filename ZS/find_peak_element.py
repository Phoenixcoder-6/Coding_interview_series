def find_peak(arr):
    ele=max(arr)
    for i in range(len(arr)):
        if arr[i]==ele:
            return i
        

arr=[1,2,3,1]
res= find_peak(arr)
print(res)