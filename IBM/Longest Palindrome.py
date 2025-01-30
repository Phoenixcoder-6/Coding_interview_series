def palindrome(s):
    if not s:
        return " "
    def expand_arond_center(left,right):
        while left >=0 and right< len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    longest=" "
    for i in range(len(s)):
        odd_palindrome=expand_arond_center(i,i)
        even_palindrome= expand_arond_center(i,i+1)

        longest= max(longest,odd_palindrome,even_palindrome,key=len)
    return longest

s="bhosdikekid"
res=palindrome(s)
print(res)
