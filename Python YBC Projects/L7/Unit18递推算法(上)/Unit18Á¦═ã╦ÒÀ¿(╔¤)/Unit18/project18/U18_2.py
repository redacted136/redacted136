import numpy as np

# 用数组存储数列，第一个元素为1，用for循环推出第10个数
nums = np.zeros(10, dtype=int)
nums[0] = 1
for i in range(1, 10):
    nums[i] = nums[i-1] + (i+1)
print(nums[9])