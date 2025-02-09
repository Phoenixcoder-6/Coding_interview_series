def longest_substring(s: str)->int:
    char_index={}
    start=0
    max_length=0

    for i,char in enumerate(s):
        if char in char_index and char_index[char]>= start:
            start= char_index[char] +1
        
        char_index[char]=i
        max_length= max(max_length, i- start + 1)
    return max_length


s= input("Enter the string:")
res= longest_substring(s)
print(res)
