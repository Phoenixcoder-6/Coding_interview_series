def long_substring(s):
    left=0
    seen=set()
    max_len=0
    start_index= 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])

        if right-left+1 > max_len:
            max_len= right - left+1
            start_index= left

    long_substring= s[start_index: start_index+ max_len]
    return max_len, long_substring


arr="abadchbahdbb"
res1,res2= long_substring(arr)
print(res1,res2)


        
        