import numpy as np

# 使用二维数组模拟落子棋盘
qp = np.zeros((7,7), dtype=int)
qp[2][4] = qp[3][4] = qp[4][3] = qp[4][4] = 1
qp[4][2] = qp[5][2] = qp[5][3] = qp[5][4] = 2

# 创建和落子棋盘形状一致的打分棋盘
score_qp = np.zeros(qp.shape, dtype=int)

# 遍历落子棋盘
for i in range(qp.shape[0]):
    for j in range(qp.shape[1]):
        # 寻找落子棋盘上所有无子的位置
        if qp[i][j] == 0:
            # 打分棋盘上对应位置为1分
            score_qp[i][j] = 1
print(score_qp)

