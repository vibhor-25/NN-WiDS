import pandas as pd
df=pd.read_csv("fruit_production.csv")
X=df[["Temperature_F","Rainfall_mm","Humidity_percent"]]
yMango=df["Mangoes_ton"]
yOrange=df["Oranges_ton"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_trainMango,y_testMango,y_trainOrange,y_testOrange=train_test_split(X,yMango,yOrange,test_size=0.2)

from sklearn.linear_model import LinearRegression
modelMango=LinearRegression(positive=True)
modelOrange=LinearRegression(positive=True)
y_predictMango=modelMango.fit(X_train,y_trainMango).predict(X_test)
y_predictOrange=modelOrange.fit(X_train,y_trainOrange).predict(X_test)

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.plot([0,max(y_testMango.max(),y_testOrange.max())],[0,max(y_testMango.max(),y_testOrange.max())],"r--")
ax.set_xlim(0,max(y_testMango.max(),y_testOrange.max()))
ax.set_ylim(0,max(y_testMango.max(),y_testOrange.max()))
ax.set_xlabel("ACTUAL PRODUCTION", fontweight="bold")
ax.set_ylabel("PREDICTED PRODUCTION",fontweight="bold")
ax.scatter(y_testMango,y_predictMango,label="MANGO PREDICTION",c="yellow")
ax.scatter(y_testOrange,y_predictOrange,label="ORANGE PREDICTION",c="Orange")
print(f"R2 Score for Mango: {modelMango.score(X_test, y_testMango):.4f}")
print(f"R2 Score for Orange: {modelOrange.score(X_test, y_testOrange):.4f}")
ax.legend()
plt.show()


