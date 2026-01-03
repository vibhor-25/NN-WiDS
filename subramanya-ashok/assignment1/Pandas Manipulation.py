
import pandas as pd
df=pd.read_csv("data_assg1.csv")
df["new column"]=pd.cut(df["value"],bins=[0,0.3,0.7,1.0],labels=["Low","Medium","High"])
df_new=df[df["new column"]!="Low"]
print(df);print(df_new)
df_new.to_csv("df_new.csv")