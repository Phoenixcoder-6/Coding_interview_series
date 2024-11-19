def palindrome(str):
    rev= str[::-1]
    if str==rev:
        return "Palindrome"
    else:
        return "Not palindrome"
    

str='abcba'
res= palindrome(str)
print(res)