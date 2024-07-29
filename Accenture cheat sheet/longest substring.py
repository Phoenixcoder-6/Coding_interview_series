def find_substring(s: str) -> int:
    char_index = {}
    start = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
    
    return max_length

string = input("Enter any string: ")
res = find_substring(string)
print(f"The length of the longest substring without repeating characters is: {res}")
