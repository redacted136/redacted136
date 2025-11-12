import numpy as np
import random

# 创建15*15棋盘
qp = np.zeros((15,15),dtype=int)
# 创建落子函数
def decision(qp, color):
    while True:
        # 棋盘范围内随机获取行索引i，列索引j
        i = random.randint(0, qp.shape[0] - 1)
        j = random.randint(0, qp.shape[1] - 1)
        # 如果该位置无棋子，则落子，并根据落子颜色赋值，跳出循环
        if qp[i][j] == 0:
            qp[i][j] = color
            break
# 第一回合落黑子
decision(qp, 1)
print(qp)
# 第一回合落白子
decision(qp, 2)
print(qp)