import numpy as np

a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10,1]])

# 按顺序遍历数组a，依次输出其中的一维数组
for i in a:
    for o in i:
        print(o)
