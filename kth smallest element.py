A=list(map(int, input().split(',')))
print("The original array:",A)
k= int(input("Enter the value of k"))
A.sort()
print(A[k-1])
