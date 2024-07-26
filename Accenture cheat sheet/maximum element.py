str=input("Enter the string:")
count=0
freq={}
def maximum(str):
    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

var=maximum(str)

maxi= max(freq, key=freq.get)
print(var, maxi)

    


