def min_repeat(s1,s2):
    repeat= -(-len(s2)//len(s1))
    temp= s1 * repeat
    if s2 in temp:
        return repeat
    elif s2 in temp+s1:
        return repeat +1
    else:
        return -1
    

s1= "abc"
s2="cabcabc"
res= min_repeat(s1,s2)
print(res)
