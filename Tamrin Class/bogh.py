import numpy as np

n=int(input("Enter the matrix size: "))
mat=np.zeros((n,n))


for i in range(n):
    one=int(input("one's count:"))
    for j in range(n):
        if j+1<=one:
            mat[n-i-1][j]=1
        else:
            mat[n-i-1][j]=0
print(mat)