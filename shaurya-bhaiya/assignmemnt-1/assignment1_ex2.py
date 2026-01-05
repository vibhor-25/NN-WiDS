import np as np
import random as rnd

matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixB = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for row in range(len(matrixA)):
    for col in range(len(matrixA[0])):
        matrixA[row][col] = rnd.randint(1, 10)
print(matrixA)
for row in range(len(matrixB)):
    for col in range(len(matrixB[0])):
        matrixB[row][col] = rnd.randint(1, 10)
print(matrixB)

addition = matrixA + matrixB
print("Addition of two matrices:\n", addition)

multiplication = np.dot(matrixA, matrixB)
print("Multiplication of two matrices:\n", multiplication)

elementwise_multiplication = matrixA * matrixB
print("Element-wise multiplication of two matrices:\n", elementwise_multiplication)

determinantA = np.linalg.det(matrixA)
print("Determinant of Matrix A:", determinantA)