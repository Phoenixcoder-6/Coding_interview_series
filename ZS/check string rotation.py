def rotation(s1,s2):
    rev= s1[::-1]
    if s2== rev:
        return True
    else:
        False

s1= "waterbottle"
s2="elttobretaw"
res= rotation(s1,s2)
print(res)