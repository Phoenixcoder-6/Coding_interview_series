def matsearch(mat,target):
    n= len(mat)
    m=len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == target:
                return ((i,j))
            
    return -1

arr=[[18, 21, 27],
     [38, 55, 67]]
rs= matsearch(arr,55)
print(rs)
            