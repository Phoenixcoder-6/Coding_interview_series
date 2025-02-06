import math
def second_smallest(arr):
    first=second=math.inf
    for num in arr:
        if num< first:
            second= first
            first=num
        elif first<num<second:
            second=num
    if second != math.inf:
        return second
    else:
        return "No second smallest element "
        
arr=[3,54,23,12,8,56]
res= second_smallest(arr)
print(res)

