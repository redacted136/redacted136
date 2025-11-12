import numpy as np


nums = np.zeros(20, dtype=int)
nums[0] = 1
nums[1] = 2
nums[2] = 4
for i in range(3, 20):
    nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
print(nums[19])