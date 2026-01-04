import pandas as pd

df = pd_read.("data_assg1.csv")

 def categorize(value):
    if 0 <= value < 0.3:
        return "Low"
    elif 0.3 <= value < 0.7:
        return "Medium"
    else:
        return "High"

 df["Category"] = df.iloc[:, 0].apply(categorize)

print(df)