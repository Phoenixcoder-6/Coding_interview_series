def subsequent(string1,string2):
    mp=' '
    i,j=0,0
    while i<len(string1) and j<len(string2):
        if string1[i]==string2[j]:
                mp+=string1[i]
                i+=1
                j+=1
    
        else:
            j+=1
    return mp

np1="abcd"
np2="abce"
result= subsequent(np1,np2)
print("Longest common subsequent is:",result)
