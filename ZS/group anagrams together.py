def anagram_group(arr):
    anagrams={}
    for word in arr:
        key="".join(sorted(word))
        if key not in anagrams:
            anagrams[key] =[]
        anagrams[key].append(word)
    return list(anagrams.values())
arr=["eat","tea","tan","ate","nat","bat"]
res= anagram_group(arr)
print(res)