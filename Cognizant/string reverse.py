def rev_string(string):
    n=len(string)
    rev=" "
    for i in range(n-1,0):
        rev+=string[i]
    return rev

string="abcd"
result= rev_string(string)
print(result)