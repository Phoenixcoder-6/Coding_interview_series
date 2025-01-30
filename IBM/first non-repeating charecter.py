def nonrepeated(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for char,count in freq.items():
        if count==1:
            return char
        
    return None
    

s="gghhij"
result= nonrepeated(s)
print(result)

        