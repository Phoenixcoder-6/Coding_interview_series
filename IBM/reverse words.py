def rev(s):
    d=[]
    r= s.split()[::-1]
    d.extend(r)
    return ' '.join(d)


s="IBM is bad"
result= rev(s)
print(result)