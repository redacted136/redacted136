import numpy as np
import random

# 创建15*15棋盘
qp = np.zeros((15,15),dtype=int)
# 创建落子函数
def decision(qp, color):
    # 棋盘范围内随机获取行索引i，列索引j
    i = random.randint(0,qp.shape[0]-1)
    j = random.randint(0,qp.shape[1]-1)
    # 根据落子颜色赋值，
    qp[i][j] = color
# 第一回合落黑子9
decision(qp, 1)
print(qp)