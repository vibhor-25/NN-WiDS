import numpy as np
import matplotlib.pyplot as plt

# y= x^3 + 2x^2 + 3x + 2

x = np.arange(10)
y = x**3 + 2*x**2 + 3*x +2

plt.plot(x,y)
plt.show()


# y = tanx/x

x = np.arange(10)
x = x[x != 0]
y = np.tan(x)/x

plt.plot(x,y)
plt.show()


# x = siny + 3y
y = np.arange(15)
x = np.sin(y) + 3*y

plt.plot(x,y)
plt.show()