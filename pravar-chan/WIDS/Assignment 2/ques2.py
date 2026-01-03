import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("house_rent_dataset.csv")
data = data.drop(["Posted On","Floor","Area Locality","Tenant Preferred","Point of Contact"], axis=1)
data = data.dropna()
X = data.drop("Rent", axis=1)
y = data["Rent"]
X = pd.get_dummies(X)
model = LinearRegression()
model.fit(X, y)
print("Model trained successfully!")
#Rent =
 # w1 * BHK
#+ w2 * Size
#+ w3 * Bathroom
#+ w4 * Is_Mumbai
#+ w5 * Is_Delhi
#+ w6 * Is_Bangalore
#+ bias (1+0+0=0+1+0=0+0+1)
