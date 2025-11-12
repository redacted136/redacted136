import numpy as np


nums = np.zeros(9, dtype=int)
# 初始条件
nums[0] = 1
nums[1] = 2
nums[2] = 3
for i in range(3, 9):
    nums[i] = nums[i-1] + nums[i-3]
print(nums) # 运行结果为：[1 2 3 4 6 9 13 19 28]