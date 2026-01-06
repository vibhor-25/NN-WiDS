import numpy as np
A=np.random.randint(0,11,size=(3,3))
B=np.random.randint(0,11,size=(3,3))
add=A+B
elementWiseMultiply=A*B
dotProduct=np.dot(A,B)
detA=np.linalg.det(A)
print("1st 3x3 array is", A)
print("2nd 3x3 array is", B)
print("sum is", add)
print("element wise product is", elementWiseMultiply)
print("dot product of A and B is", dotProduct)
print("determinant of A is", detA)
