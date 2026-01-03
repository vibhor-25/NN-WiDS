import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f(x, M, C):
    z=np.dot(x,M) +C
    return 1/(1+np.exp(-z))

def J(x, y, M, C):
    n = y.shape[0]
    return -(1 / n) * (np.dot(y,np.log(f(x, M, C))) + np.dot(1-y,np.log(1-f(x,M,C))))

def gradients(x, y, M, C):
    n = y.shape[0]
    dM = -(1 / n) * np.dot(x.T,y-f(x,M,C))
    dC = -(1 / n) * np.sum(y-f(x,M,C))
    return dM, dC

data=pd.read_csv("log_reg.csv")
x=data[['x','y','color']].values
plt.scatter(x[:,0],x[:,1])
x[:,0]=np.multiply(x[:,0],x[:,0])
M = np.zeros(x.shape[1]-1) 
C = 0.0
lr = 0.01
epochs = 10000
prev_cost = float('inf')

for i in range(epochs):
    dM, dC = gradients(x[:,0:2], x[:,2], M, C)  
    M -= lr * dM
    C -= lr * dC
    cost = J(x[:,0:2], x[:,2], M, C)
    if abs(prev_cost - cost) < 0.0001 and cost > prev_cost:
        break       
    if(i % 20 == 0) :
        print(cost)
    prev_cost = cost
print("Final Weights (scaled features):", M)
print("Final Bias:", C)
x_1=np.linspace(-5, 5, 100)
y=-(C+M[0]*(x_1**2))/M[1]
plt.plot(x_1,y)
plt.show()



