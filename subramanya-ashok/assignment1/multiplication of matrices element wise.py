import numpy as np
import pandas as pd
AE=np.random.randint(1,10,(3,3))
BE=np.random.randint(1,10,(3,3))
elementwise=AE*BE
EW=np.zeros((3,3))
for i in range(3):
     for j in range(3):
          EW[i][j]=AE[i][j]*BE[i][j]

print(elementwise);print(EW)