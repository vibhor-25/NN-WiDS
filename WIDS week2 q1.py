import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("fruit_production.csv")

X = df[['Temperature_F', 'Rainfall_mm', 'Humidity_percent']]
Y = df['Mangoes_ton']
Z = df['Oranges_ton']

model = LinearRegression()


model.fit(X,Y)
model.fit(X,Z)

print("model coffecient", model.coef_)

