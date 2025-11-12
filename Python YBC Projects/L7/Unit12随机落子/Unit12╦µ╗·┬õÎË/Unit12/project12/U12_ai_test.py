import numpy as np
import random

class AIPlayer():
    # 创建__init_函数初始化棋子颜色属性
    def __init__(self, clr):
        self.color = clr
    # 创建落子函数
    def decision(self, qp):
        # while循环，条件为True
        while True:
            # 棋盘范围内随机获取行索引i，列索引j
            i = random.randint(0, qp.shape[0] - 1)
            j = random.randint(0, qp.shape[1] - 1)
            # 如果该位置无棋子，记录该位置，跳出循环
            if qp[i][j] == 0:
                pos = [i, j]
                break
        # 返回落子位置
        return pos
# 生成实例：myAI，传入参数0
myAI = AIPlayer(0)