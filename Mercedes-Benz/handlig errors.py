def addition(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    else:
        print("Not a valid number")

try:
    a=int(input("Enter first input:"))
    b=int(input("Enter second input:"))
    res=addition(a,b)
    if res is not None:
        print("The addition value is:",res)
except ValueError:
    print("Invalid input")