import numpy as np

a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 1]])
s = a.shape
# 按顺序遍历数组a，依次输出各元素的值
for o in range(s[0]):
    for i in range(s[1]):
        print(a[o][i])

