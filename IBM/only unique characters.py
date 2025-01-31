def unique_characters(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for j in freq.items():
        if freq[i]>1:
            return False
        else:
            return True
        
    return None


s="abcdef"
res= unique_characters(s)
print(res)