import numpy as np


nums = np.zeros(20, dtype=int)
nums[0] = 1
nums[1] = 2
for i in range(2, 20):
    nums[i] = nums[i-1] + nums[i-2]
print(nums[19])