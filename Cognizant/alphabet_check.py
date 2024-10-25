digits=input("Enter the digits:")
for i in range(0,len(digits),2):
    num=int(digits[i:i+2])
    result= chr(num-65+ord('A'))
    print(f"{num}---->{result}")