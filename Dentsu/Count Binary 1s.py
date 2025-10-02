def count_1s(num):
    binary= bin(num)[2:]
    count=0
    for i in binary:
        if i=="1":
            count+=1
    return count

num=19
res= count_1s(num)
print(res)