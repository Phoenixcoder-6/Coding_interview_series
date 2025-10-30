def substring(s,sub):
    for i in range(len(s)- len(sub)+1):
        if s[i:i+len(sub)]==sub:
            start=i
            end= i+len(sub)-1

        return start,end
    
arr1="abcde"
arr2= "ab"
res1,res2= substring(arr1,arr2)
print(res1,res2)