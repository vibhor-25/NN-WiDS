import pandas as pd
import numpy as np


# 1."fruit production"

df=pd.read_csv("fruit_production.csv")
ym = df["Mangoes_ton"].values
yo=df["Oranges_ton"].values
X = df[["Temperature_F", "Rainfall_mm", "Humidity_percent"]].values
#feature scaling
x_mean=X.mean(axis=0)
x_std=X.std(axis=0)
X=(X-x_mean)/x_std
l=0.002
w=np.zeros(X.shape[1])
b=0
# for mangoes 
for k in range(1000):
     db=0;dw=np.zeros(X.shape[1])
     for i in range(X.shape[0]):     
         e=(np.dot(X[i],w)+b)-ym[i]
         for j in range(X.shape[1]):
             dw[j]+=e*X[i][j]
         db+=e
     dw=dw/X.shape[0]
     db=db/X.shape[0]    
     w-=l*dw
     b-=l*db    

# for oranges 

wo=np.zeros(X.shape[1])
bo=0
for k in range(1000):
     db1=0;dw1=np.zeros(X.shape[1])
     for i in range(X.shape[0]):     
         e1=(np.dot(X[i],wo)+bo)-yo[i]
         for j in range(X.shape[1]):
             dw1[j]+=e1*X[i][j]
         db1+=e1
     dw1=dw1/X.shape[0]
     db1=db1/X.shape[0]    
     wo-=l*dw1
     bo-=l*db1  

print(F"for mangoes the w vector is {w} and b is {b}")
print(F"for oranges the w vector is {wo} and b is {bo}")

yp=np.zeros(5)
for i in range (5):
    yp[i]=np.dot(X[i],w)+b

print(yp) 