# %% [markdown]
# excercise 1

# %%
for i in range(1,101) :
            if (i % 3 == 0) :
                if(i % 5 == 0) :
                    print("FizzBuzz")
                    continue
                else :
                    print("Fizz")
                    continue
            if (i % 5 ==0) :
                print("Buzz")
            else :
                print(i)

# %% [markdown]
# exercise-2

# %%
import numpy as np
A=np.random.randint(2,9,(3,3))
B=np.random.randint(2,9,(3,3))
print(A)
print(B)
print(np.add(A,B))
print(np.multiply(A,B))
print(np.dot(A,B))
print(np.linalg.det(A))

# %% [markdown]
# exercise-3
# 

# %%
import pandas as pd
df= pd.read_csv("data_assg1.csv")
df["result"]="None"
df.loc[(df["value"] < 0.3) & (df["value"] > 0),"result"] ="low"
df.loc[(df["value"] < 0.7) & (df["value"] > 0.3),"result"] ="medium"
df.loc[(df["value"] < 1) & (df["value"] > 0.7),"result"] ="high"
df.drop(df[df["result"]=="low"].index,inplace=True)
df.to_csv("data_assg1.csv",index=False)
print(df)

# %% [markdown]
# exercise-4

# %%
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-50, 50, 100)   # x values
y = x**3+2*x**2+3*x+2
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=x^3+2x^2+3x+2")
plt.show()
x=np.linspace(-10, 10, 100)
x=x[x!=0]
y = np.tan(x)/x

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = (tan x)/x")
plt.show()

y=np.linspace(-30, 30, 200)
x = np.sin(y)+3*y

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("x = sin y + 3y")
plt.show()


