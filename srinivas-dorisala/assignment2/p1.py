import pandas as pd
import numpy as np


def f(x, M, C):
    return np.dot(x, M) + C

def J(x, y, M, C):
    n = len(y)
    return (1 / (2 * n)) * np.sum((f(x, M, C) - y) ** 2)

def gradients(x, y, M, C):
    n = len(y)
    y_p = f(x, M, C)
    
    dM = (1 / n) * np.dot(x.T, (y_p - y))
    dC = (1 / n) * np.sum(y_p - y)
    
    return dM, dC

data = pd.read_csv("fruit_production.csv")
X = data[['Temperature_F', 'Rainfall_mm', 'Humidity_percent']].values
y = data['Mangoes_ton'].values

X_mean = X.mean(axis=0)
X_std = X.std(axis=0)

X_scaled = (X - X_mean) / X_std
M = np.zeros(X.shape[1])   
C = 0.0
lr = 0.01
epochs = 10000

prev_cost = float('inf')

for i in range(epochs):
    dM, dC = gradients(X_scaled, y, M, C)  
    M -= lr * dM
    C -= lr * dC
    cost = J(X_scaled, y, M, C)
    if abs(prev_cost - cost) < 0.0001 and cost > prev_cost:
        break       
    if(i % 20 == 0) :
        print(cost)
    prev_cost = cost
print("Final Weights (scaled features):", M)
print("Final Bias:", C)
