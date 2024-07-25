arr=[]
n= int(input("Enter the number of terms you want to enter:"))
for i in range (n):
    num= int(input(f"Enter the array elements at position {i+1}:"))
    arr.append(num)

sorted_array=sorted(arr)
print(sorted_array)