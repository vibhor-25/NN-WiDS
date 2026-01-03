import pandas as pd #"used to read and play around with csv files"
from sklearn.model_selection import train_test_split #"ML library containing regression algorithms splits the data set"
from sklearn.linear_model import LinearRegression # 1/(1+e^-(wx+b)) for 0 or 1 cases 
#20 percent testing 80 percent training 
from sklearn.metrics import mean_squared_error
fruit= pd.read_csv("fruit_production (1).csv")#we read the file
print("Fruit data loaded")
print(fruit.head())
print(fruit.columns)
Xfruit = fruit[['Area', 'Rainfall', 'Temperature']]
yfruit = fruit['Production']
Xf_train, Xf_test, yf_train, yf_test = train_test_split(Xfruit, yfruit, test_size=0.2)# 20 percent testing  -80 percent training
fruitxmodel = LinearRegression()#empty model created
fruitxmodel.fit(Xf_train, yf_train)#model trained
yf_pred = fruitxmodel.predict(Xf_test)#prediction 
fruit_error = mean_squared_error(yf_test, yf_pred)#error
print("Fruit Production MSE:", fruit_error)
print("Fruit Model Coefficients:", fruitxmodel.coef_)
print("Fruit Model Intercept:", fruitxmodel.intercept_)
