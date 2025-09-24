import CNN_AI
import numpy as np

path = 'dog.jpg'      # 原图像路径

kkk = np.array([[0, 0, 1, 0, 0],
                [0, 1, 2, 1, 0],
                [1, 2, -16, 2, 1],
                [0, 1, 2, 1, 0],
                [0, 0, 1, 0, 0]])

CNN_AI.convolution(path,kkk)     # 填入正确参数
