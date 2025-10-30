def duplicate_charecters(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    max_fr=0
    max_char=''
    for item,fr in freq.items():
        if fr>max_fr:
            max_fr = fr
            max_char=item
    return max_char
        
arr="aabbbcc"
res= duplicate_charecters(arr)
print(res)
