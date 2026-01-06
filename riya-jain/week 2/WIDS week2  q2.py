import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_rent_dataset.csv")

df['Furnishing Status'] = df['Furnishing Status'].map({
    'Unfurnished': 0,
    'Semi-Furnished' : 0,
    'Furnished': 1
    })

X = df[['BHK','Size','Furnishing Status','Bathroom']]
Y = df['Rent']

model = LinearRegression()

model.fit(X,Y)

print("model coffecient", model.coef_)