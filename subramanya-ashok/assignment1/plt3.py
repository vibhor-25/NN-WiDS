import numpy as np
import matplotlib.pyplot as plt
y=np.linspace(-20,20,1000)
x=np.sin(y)+3*y
plt.plot(x,y)
plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.show()