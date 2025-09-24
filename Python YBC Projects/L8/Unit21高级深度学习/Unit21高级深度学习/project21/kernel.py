import CNN_AI
import numpy as np
path = 'flower.jpg'      # 原图像路径
#kernel1 是一个边缘特征提取器
#kernel2 是一个浮雕特征提取器
#kernel3 是一个锐化特征提取器

kernel1 = np.array([[1, 1, 1],
                    [1, -7.5, 1],
                    [1, 1, 1]])

kernel2 = np.array([[-1, -1, -1, -1, 0],
                    [-1, -1, -1, 0, 1],
                    [-1, -1, 0, 1, 1],
                    [-1, 0, 1, 1, 1],
                    [0, 1, 1, 1, 1]])

kernel3 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

CNN_AI.convolution(path, kernel3)