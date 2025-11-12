import numpy as np

# 用数组存储数列，第一个元素为1，用for循环推出第8个数
nums = np.zeros(8, dtype=int)
nums[0] = 1
for i in range(1, 8):
    nums[i] = 2* nums[i-1] + 1
print(nums[7])