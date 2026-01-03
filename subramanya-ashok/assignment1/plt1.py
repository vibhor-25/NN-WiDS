import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,100)
y=x**3+2*x**2+3*x+2
plt.plot(x,y)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.show()