def majority_element(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i] +=1
        else:
            freq[i]=1

    max_freq= 0
    n= len(arr)
    for item, fr in freq.items():
        if fr > max_freq:
            max_freq= fr
            max_elem= item
    return max_freq, max_elem

arr= [1,1,1,1,4,5,6,9]
res= majority_element(arr)
print(res)
