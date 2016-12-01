INPUT(Matrix)
    B <- INPUT Matrix
    C <- INPUT Matrix

ADD(B,C)
    for i<-0 to n                    #n
        for j<-0 to n               #n*n
            A[i][j] <- B[i][j]+C[i][j]

    return A

MULTIPYCONSTANT(A, p)
    for i<-0 to n                #n
        for j<-0 to n            #n*n
            A[i][j] <- ADD[i][j]*P
            
    return A

MULTIPLYMATRIX(B,C)
    for i<-0 to n                #n
        for j<-0 to n            #n*n
            for k<-0 to n        #n*n*n
                value <-  B[i,k]*C[k,j]
                res[i][j] <-res[i][j] + value
    return res

SUBTRACT(B,C)
    for i<-0 to n                #n
        for j<-0 to n            #n*n
            A[i][j] <- B[i][j] - C[i][j]

    return A

R1 <- MULTIPLYMATRIX(B,C)
R2 <- ADD(B,C)
R3 <- SUBTRACT(B,C)
R4 <- MULTIPLYCONSTANT(A,2)
R <- B*C + 2*(B+C)
#Big O Notation = n*n*n
