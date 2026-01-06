import pandas as pd
df=pd.read_csv("log_reg.csv")
df["x1"]=df["x"]*df["x"]
X=df[["x","x1","y"]]
y=df["color"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train, y_train)
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
print(f"Training Accuracy: {train_acc:.2%}")
print(f"Testing Accuracy: {test_acc:.2%}")