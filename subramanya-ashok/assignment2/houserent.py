# 2. linear regression on given data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def lrm(X,ym):
   x_mean=X.mean(axis=0)
   x_std = X.std(axis=0)
   x_std[x_std == 0] = 1

   X=(X-x_mean)/x_std
   l=0.002
   w=np.zeros(X.shape[1])
   b=0
   for k in range(400):
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

   return  w,b,x_mean, x_std


def predict(X_new, w, b, mean, std):
    X_new = (X_new - mean) / std
    return np.dot(X_new, w) + b

df=pd.read_csv("house_rent_dataset.csv")
y_rent=df["Rent"].values  
X=df.drop(columns=["Rent"])
df=df.drop('Rent',axis=1)
encoder=OneHotEncoder(drop='first',sparse_output=False)
city_enc=encoder.fit_transform(df[["City"]])
city_cols=encoder.get_feature_names_out(["City"])
city_df=pd.DataFrame(city_enc,columns=city_cols,index=df.index)
df=pd.concat([df,city_df],axis=1)
df=df.drop("City",axis=1)

def sfloor(s):
    if pd.isna(s):
        return 0, 0

    s = str(s).strip()
    if "out of" not in s:
        if "Upper Basement" in s:
            return -1, 0
        elif "Lower Basement" in s:
            return -2, 0
        elif "Ground" in s:
            return 0, 0
        else:
            return int(s), 0

    t = int(s.split("out of")[1].strip())

    if "Upper Basement" in s:
        c = -1
    elif "Lower Basement" in s:
        c = -2
    elif "Ground" in s:
        c = 0
    else:
        c = int(s.split("out of")[0].strip())

    return c, t

df[["current floor","total floor"]]=df["Floor"].apply(
    lambda x: pd.Series(sfloor(x)))  
df=df.drop("Floor",axis=1)   
furnish_map = {
    "Unfurnished": 0,
    "Semi-Furnished": 1,
    "Furnished": 2
}
df["Furnishing Status"]=df["Furnishing Status"].map(furnish_map)
areat_map={
    'Super Area': 1, 'Carpet Area': 3, 'Built Area': 2
}
df['Area Type']=df['Area Type'].map(areat_map)
ohe=OneHotEncoder(drop="first",sparse_output=False)
area_l=ohe.fit_transform(df[["Area Locality"]])
arcl=ohe.get_feature_names_out(["Area Locality"])
area_le=pd.DataFrame(area_l,columns=arcl,index=df.index)
df=pd.concat([df,area_le],axis=1)
df=df.drop('Area Locality',axis=1)
a = df.drop(columns=["Posted On",'Tenant Preferred','Point of Contact']).to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    a, y_rent, test_size=0.2, random_state=42
)

w, b, X_m, X_std = lrm(X_train, y_train)
prediction = predict(X_test, w, b, X_m, X_std)

print(prediction)