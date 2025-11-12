import numpy as np
import random

# 使用二维数组模拟落子棋盘
qp = np.zeros((7,7), dtype=int)
qp[2][4] = qp[3][4] = qp[4][3] = qp[4][4] = 1
qp[4][2] = qp[5][2] = qp[5][3] = qp[5][4] = 2
qp[1][4] = 1
qp[0][4] = 2

# 数组边界判定
def check(qp, i_next, j_next):
    if 0 <= i_next <= qp.shape[0]-1:
        if 0 <= j_next <= qp.shape[1]-1:
            return True
    else:
        return False

# 获取4个方向连珠数的最大值
def get_score(qp, i, j):
    # 统计横向连珠数count1
    count1 = 1
    for step in range(1, 5):
        i_next = i
        j_next = j + step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count1 += 1
            else:
                break
    for step in range(1, 5):
        i_next = i
        j_next = j - step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count1 += 1
            else:
                break
    # 统计纵向连珠数count2
    count2 = 1
    for step in range(1, 5):
        i_next = i + step
        j_next = j
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count2 += 1
            else:
                break
    for step in range(1, 5):
        i_next = i - step
        j_next = j
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count2 += 1
            else:
                break
    # 统计斜向1连珠数count3
    count3 = 1
    for step in range(1, 5):
        i_next = i + step
        j_next = j + step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count3 += 1
            else:
                break
    for step in range(1, 5):
        i_next = i - step
        j_next = j - step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count3 += 1
            else:
                break
    # 统计斜向2连珠数count4
    count4 = 1
    for step in range(1, 5):
        i_next = i - step
        j_next = j + step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count4 += 1
            else:
                break
    for step in range(1, 5):
        i_next = i + step
        j_next = j - step
        if check(qp, i_next, j_next):
            if qp[i_next][j_next] == qp[i][j]:
                count4 += 1
            else:
                break

    # 取4个连珠数中的最大值
    max_count = max(count1, count2, count3, count4)
    return max_count

# 创建和落子棋盘形状一致的打分棋盘
score_qp = np.zeros(qp.shape, dtype=int)

# 遍历落子棋盘
for i in range(qp.shape[0]):
    for j in range(qp.shape[1]):
        # 寻找落子棋盘上所有无子的位置
        if qp[i][j] == 0:
            # 假设AI程序在棋盘上该位置落子
            qp[i][j] = 1
            # 使用get_score函数获取该位置连珠数的最大值
            score = get_score(qp, i, j)
            # 把最大值作为分数存储到打分棋盘对应位置
            score_qp[i][j] = score
            # 实际上还没落子，不能改变落子棋盘，需要还原落子棋盘
            qp[i][j] = 0
print(score_qp)

# 获取打分棋盘的最高分
max_score = np.max(score_qp)

lst = []
# 遍历打分棋盘
for i in range(score_qp.shape[0]):
    for j in range(score_qp.shape[1]):
        # 获取打分棋盘最高分对应的所有位置
        if score_qp[i][j] == max_score:
            lst.append([i,j])
# 从多个位置中随机选取一个位置落子
pos = random.choice(lst)
print(pos)
