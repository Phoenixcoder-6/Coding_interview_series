def check_anagram(string1,string2):
    s1= sorted(string1.lower())
    s2= sorted(string2.lower())

    if s1==s2:
        return "Anagram"
    else:
        return None
    
res=check_anagram('Silent','Listen')
print(res)
