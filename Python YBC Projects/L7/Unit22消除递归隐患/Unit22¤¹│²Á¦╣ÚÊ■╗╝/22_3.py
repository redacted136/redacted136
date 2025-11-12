import numpy as np


wg = np.zeros((3,7), dtype = int)
for j in range(1,7):
    wg[0][j] = 1
for i in range(1, 3):
    wg[i][0] = 1
for i in range(1, 3):
    for j in range(1, 7):
        # 递推关系
        wg[i][j] = wg[i-1][j] + wg[i][j-1]
print(wg[2][6])