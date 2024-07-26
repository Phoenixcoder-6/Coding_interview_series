arr=[]
n= int(input("Enter the number of terms you want to enter:"))
for i in range (n):
    num= int(input(f"Enter the array elements at position {i+1}:"))
    arr.append(num)

arr= list(set(arr))
print(arr)