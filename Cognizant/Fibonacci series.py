def fibonacci(n):
    head=0
    head2=1
    lst=[head,head2]
    for i in range(2,n):
        next= head+head2
        lst.append(next)
        head=head2
        head2=next
    return lst

result= fibonacci(5)
print(result)
