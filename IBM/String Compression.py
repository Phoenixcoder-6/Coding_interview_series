def compressString(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    compressed_parts = [f"{char}{count}" for char, count in freq.items()] 
    compressed = ''.join(compressed_parts)  # Join the parts into a single string
    return compressed

s="aabbc"
res=compressString(s)
print(res)
