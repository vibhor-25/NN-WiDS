import pandas as pd
df=pd.read_csv("house_rent_dataset.csv")
dfEncoded=pd.get_dummies(df, columns=["Area Type", "Furnishing Status","City"], drop_first=True)
X=dfEncoded[["BHK","Size","Area Type_Carpet Area","Area Type_Super Area","Furnishing Status_Semi-Furnished","Furnishing Status_Unfurnished","City_Chennai","City_Delhi","City_Hyderabad","City_Kolkata","City_Mumbai"]]
y=df["Rent"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
model=LinearRegression(positive=True)
yPredict=model.fit(X_train,y_train).predict(X_test)

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.plot([0,max(y_test.max(),yPredict.max())],[0,max(y_test.max(),yPredict.max())],"r--")
ax.set_xlim(0,yPredict.max())
ax.set_ylim(0,yPredict.max())
ax.set_xlabel("ACTUAL RENT", fontweight="bold")
ax.set_ylabel("PREDICTED RENT",fontweight="bold")
ax.scatter(y_test,yPredict,label="RENT PREDICTION",c="blue")
print(f"R2 Score: {model.score(X_test, y_test):.4f}")
ax.legend()
plt.show()