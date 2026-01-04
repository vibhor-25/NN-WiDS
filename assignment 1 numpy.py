import numpy as np

a = np.random.randint(1,10, size=(3,3))
b = np.random.randint(1,10, size=(3,3))

print(a)
print(b)

#addition of a and b

r = a + b
print(r)

#element wise multiplication of a and b

p = a*b
print(p)

#dot product of a and b

q = np.dot(a,b)
print(q)

#determinant of matrix a

s = np.linalg.det(a)
print(s)