input_string = input("Enter the string:")
freq = {}
def occurance(input_string):
    for char in input_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

occurrences = occurance(input_string)
print(occurrences)
