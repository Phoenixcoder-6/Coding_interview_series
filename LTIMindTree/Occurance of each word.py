import re
def check(string):
    # Remove punctuation
    string = re.sub(r'[^\w\s]', '', string)
    arr= string.split(" ")
    freq={}
    for word in arr:
        word= word.lower()
        if word in freq:
            freq[word] +=1
        else:
            freq[word]=1

    return freq

string= "I love India. India is great."
res= check(string)
print(res)