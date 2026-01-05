import matplotlib.pyplot as mpl
import np as np

x = np.linspace(-50,50,1000)
y = x**3 + 2*x**2 + 3*x + 2

mpl.plot(x,y)
mpl.show()

'''
x = np.linspace(-50,50,1000)
x=x[x!=0]
y=np.tan(x)/x

y = np.linspace(-50,50,1000)
x=np.sin(y)/y + 3y 
'''