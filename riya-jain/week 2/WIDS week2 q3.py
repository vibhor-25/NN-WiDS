import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("log_reg.csv")

X = df[['x','y']]
Y = df['color']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state= 42
)

model = LogisticRegression()
model.fit(X_train, Y_train)

traing_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Trainging Accuracy:", accuracy_score(Y_train, traing_pred))
print("testing accuracy:", accuracy_score(Y_test, test_pred))

