def bit_flip(a,b):
    binary_a= bin(a)[2:]
    binary_b= bin(b)[2:]

    max_len= max(len(binary_a),len(binary_b))
    binary_a= binary_a.zfill(max_len)
    binary_b= binary_b.zfill(max_len)
    count=0
  
    for i in range(max_len):
        if binary_a[i] != binary_b[i]:
            count+=1
    return count

num1= 10
num2= 20
res1= bit_flip(num1,num2)
print(res1)