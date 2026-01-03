import numpy as np
import pandas as pd

a=int(input("enter row of A "));b=int(input("enter common column/row "));c=int(input("enter column of B "))
A=np.random.randint(1,10,(a,b))
B=np.random.randint(1,10,(b,c))
print(A); print(B)
product=np.zeros((a,c))

for i in range(a):
        for j in range(c):
            for k in range(b):
                product[i][j]+=A[i][k]*B[k][j]

Product=np.matmul(A,B)
if((product==Product).all()):
    print("both matched")
    print(product); print(Product)