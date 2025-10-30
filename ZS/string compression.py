def string_compress(s):
    #aaabccd -> a3bc2d
    count=1
    res=" "
    for i in range(1,len(s)):
        if s[i]== s[i-1]:
            count+=1
        else:
            res+= s[i-1] +(str(count) if count > 1 else "")
            count=1

    res+= s[-1] + (str(count) if count > 1 else " ")
    return res
    
s="aaabbcc"
res=string_compress(s)
print(res)
        
