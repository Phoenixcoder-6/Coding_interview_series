str=input("Enter a string:")
rev= str[ ::-1]
def palindrome(str):
    if str== rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome(str)