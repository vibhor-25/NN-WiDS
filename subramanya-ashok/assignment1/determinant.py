import numpy as np

def determinant(A,n):
    det=0
    if(n==2):
        return ((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))


    for j in range(n):
       B=np.delete(np.delete(A,0,0),j,1)
       det+=(((-1)**j)*A[0][j]*determinant(B,B.shape[0]))
    return det

a=int(input("enter row=column for square matrix "))
Sq=np.random.randint(1,10,(a,a))

print(Sq)
print(determinant(Sq,a));print(np.linalg.det(Sq))