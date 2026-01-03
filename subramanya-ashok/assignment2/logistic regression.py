# 3. logistic regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("log_reg.csv")

X = df[["x", "y"]].values   
y = df["color"].values       

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

print("Predicted classes (first 10):")
print(y_pred[:10])
print("Actual classes (first 10):")
print(y_test[:10])


print("Predicted probabilities (first 5):")
print(y_prob[:5])