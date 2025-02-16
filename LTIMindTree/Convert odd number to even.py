def odd_even(string):
    n= len(string)
    arr=[]
    for i in range(n):
        for j in range(i+1,n):
            num= list(string)
            num[i],num[j] = num[j],num[i]
            num2= int("".join(num))

            if num2%2==0:
                arr.append(num2)

    return max(arr) if arr else -1


string='9834'
res= odd_even(string)
print(res)

