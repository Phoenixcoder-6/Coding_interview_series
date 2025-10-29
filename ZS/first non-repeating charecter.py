def first_char(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for item,fr in freq.items():
        if fr==1:
            return item
        
arr= "swiss"
res= first_char(arr)
print(res)