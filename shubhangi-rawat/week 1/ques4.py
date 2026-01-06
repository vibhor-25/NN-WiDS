import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,5)
y=np.arange(1,5)

y1=(x**3)+2*(x**2)+(3*x)+2
y2=(np.tan(x))/x
x1=np.sin(y)+(3*y)

plt.plot(x,y1, label="y=x^3+2x^2+3x+2", c="r")
plt.plot(x,y2,label="y=(tan x)/x", c="b")
plt.plot(x1,y,label="x=sin y+3y", c="g")

plt.legend()
plt.show()