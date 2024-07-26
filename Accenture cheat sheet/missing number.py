arr=[]
n= int(input("Enter the number of elements you want to enter:"))
for i in range(n):
    num=int(input(f"Enter the element in position {i+1}:"))
    arr.append(num)
print("Original array is :", arr)

expected_sum= sum(arr)
print(expected_sum)

arr2=[]
n2= int(input("Enter the given array length:"))

for j in range(n2):
    num2= int(input())
    arr2.append(num2)

original_sum= sum(arr2)

missing_value= expected_sum-original_sum

print("The missing value is:",missing_value)

