start=int(input("Enter the first number:"))
end= int(input("Enter the last number:"))

sum=0
for i in range(start,end+1):
    sum=sum+i

print(sum)