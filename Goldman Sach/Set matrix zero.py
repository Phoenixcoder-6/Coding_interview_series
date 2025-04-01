def setzeroes(matrix):
    if not matrix:
        return
    
    m,n= len(matrix),len(matrix[0])
    is_col_zero= False #tracks if first column should be zero
    is_row_zero= False #tracks if first row should be zero
    
    # Check the matrix
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                if i==0:
                    is_row_zero = True
                if j==0:
                    is_col_zero= True

                matrix[0][j]=0
                matrix[i][0]=0

    #Set inner matrix elements based on markers

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j]==0:
                matrix[i][j]=0


    if is_row_zero:
        for j in range(n):
            matrix[0][j] =0

    if is_col_zero:
        for i in range(m):
            matrix[i][0]=0


    return matrix




arr=[[1,0,1],[1,1,1],[1,1,1]]
print(setzeroes(arr))



    
