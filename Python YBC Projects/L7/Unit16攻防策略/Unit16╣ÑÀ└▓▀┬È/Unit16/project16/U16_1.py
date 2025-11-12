from U16_game import start_game
import numpy as np
import random

class AIPlayer():
    def __init__(self, clr):
        self.color = clr  # black:1, white:2

    # 数组边界判定
    def check(self, qp, i_next, j_next):
        if 0 <= i_next <= qp.shape[0] - 1:
            if 0 <= j_next <= qp.shape[1] - 1:
                return True
        else:
            return False

    # 获取4个方向连珠数的最大值
    def get_score(self, qp, i, j):
        # 统计横向连珠数count1
        count1 = 1
        for step in range(1, 5):
            i_next = i
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count1 += 1
                else:
                    break
        for step in range(1, 5):
            i_next = i
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count1 += 1
                else:
                    break
        # 统计纵向连珠数count2
        count2 = 1
        for step in range(1, 5):
            i_next = i + step
            j_next = j
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count2 += 1
                else:
                    break
        for step in range(1, 5):
            i_next = i - step
            j_next = j
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count2 += 1
                else:
                    break
        # 统计斜向1连珠数count3
        count3 = 1
        for step in range(1, 5):
            i_next = i + step
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count3 += 1
                else:
                    break
        for step in range(1, 5):
            i_next = i - step
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count3 += 1
                else:
                    break
        # 统计斜向2连珠数count4
        count4 = 1
        for step in range(1, 5):
            i_next = i - step
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count4 += 1
                else:
                    break
        for step in range(1, 5):
            i_next = i + step
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count4 += 1
                else:
                    break

        # 取4个连珠数中的最大值
        max_count = max(count1, count2, count3, count4)
        return max_count

    # 落子函数
    def decision(self, qp):
        # 创建和落子棋盘形状一致的我方打分棋盘
        my_score_qp = np.zeros(qp.shape, dtype=int)
        # 创建和落子棋盘形状一致的对方打分棋盘
        his_score_qp

        # 遍历落子棋盘
        for i in range(qp.shape[0]):
            for j in range(qp.shape[1]):
                # 寻找落子棋盘上所有无子的位置
                if qp[i][j] == 0:
                    # 假设AI程序在棋盘上该位置落子
                    qp[i][j] = self.color
                    # 使用get_score函数获取我方该位置连珠数的最大值
                    my_score = self.get_score(qp, i, j)
                    # 把最大值作为分数存储到我方打分棋盘对应位置
                    my_score_qp[i][j] = my_score

                    # 对方执子颜色
                    hiscolor = 0
                    if self.color == 1:
                        hiscolor = 2
                    else:
                        hiscolor = 1
                    # 假设对方在棋盘上该位置落子
                    qp[i][j] = ?
                    # 使用get_score函数获取对方该位置连珠数的最大值
                    his_score = ?
                    # 把最大值作为分数存储到打分棋盘对应位置
                    his_score_qp[i][j] = ?

                    # 实际上还没落子，不能改变落子棋盘，需要还原落子棋盘
                    qp[i][j] = 0

        # 获取打分棋盘的最高分
        max_score = np.max(score_qp)

        # 遍历打分棋盘
        lis1 = []
        for i in range(score_qp.shape[0]):
            for j in range(score_qp.shape[1]):
                # 获取打分棋盘最高分对应的所有位置
                if score_qp[i][j] == max_score:
                    lis1.append([i, j])
        # 从多个位置中随机选取一个位置落子
        pos = random.choice(lis1)
        return pos

myAI = AIPlayer(1)
start_game(myAI)