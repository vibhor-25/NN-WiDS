import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,200)
y = np.tan(x) / x
x = x[x != 0]
y[np.abs(y) > 70] = np.nan
plt.plot(x,y)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.show()