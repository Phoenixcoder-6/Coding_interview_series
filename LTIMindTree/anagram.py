from collections import Counter
def check_anagram(s1,s2):
    #if set(s1.lower())==set(s2.lower()):  set only checks if there is the similar charecters or not, they ignores the frequenct
    if Counter(s1.lower()) == Counter(s2.lower()):
        return "Anagram"
    else:
        return "Not anagram"
    

s1= "Listen"
s2= "Silent"
res= check_anagram(s1,s2)
print(res)