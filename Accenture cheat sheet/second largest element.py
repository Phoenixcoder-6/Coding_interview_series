
def find_numbers(arr):
    n= int(input("Enter the number of elements you want to enter in that array:"))
    for i in range(n):
        num= int(input(f"Enter the value at position {i+1}:" ))
        arr.append(num)
        arr.sort()
    rt= arr[-2]
    return (rt)


arr=[]

res= find_numbers(arr)
print("The second largest element is:", res)