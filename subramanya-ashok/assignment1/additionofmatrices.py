import numpy as np
import pandas as pd
AS=np.random.randint(1,10,(3,3))
BS=np.random.randint(1,10,(3,3))
_sum=AS+BS
SUM=np.zeros((3,3))
for i in range(3):
     for j in range(3):
          SUM[i][j]=AS[i][j]+BS[i][j]

print(SUM);print(_sum)