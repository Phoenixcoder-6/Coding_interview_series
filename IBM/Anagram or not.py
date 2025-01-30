def anagram(s,a):
    if set(s.lower())==set(a.lower()):
        return("Anagram")
    else:
        return("Not Anagram")
    
res= anagram("Silent","Listen")
print(res)