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

    # 获取打分棋盘最高分对应的所有位置
    def get_pos1(self, score_qp, max_score):
        lst = []
        for i in range(score_qp.shape[0]):
            for j in range(score_qp.shape[1]):
                if score_qp[i][j] == max_score:
                    lst.append([i, j])
        return lst

    # 获取在max_pos这些位置上的最大值
    def get_max(self, score_qp, max_pos):
        max_score = 0
        for p in max_pos:
            if score_qp[p[0]][p[1]] > max_score:
                max_score = score_qp[p[0]][p[1]]
        return max_score

    # 获取最大值所在的所有位置，随机落子
    def get_pos2(self, score_qp, max_pos, max_score):
        lst = []
        for p in max_pos:
            if score_qp[p[0]][p[1]] == max_score:
                lst.append(p)
        pos = random.choice(lst)
        return pos

    # 落子函数
    def decision(self, qp):
        # 创建和落子棋盘形状一致的我方打分棋盘
        my_score_qp = np.zeros(qp.shape, dtype=int)
        # 创建和落子棋盘形状一致的对方打分棋盘
        his_score_qp = np.zeros(qp.shape, dtype=int)

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
                    qp[i][j] = hiscolor
                    # 使用get_score函数获取对方该位置连珠数的最大值
                    his_score = self.get_score(qp, i, j)
                    # 把最大值作为分数存储到打分棋盘对应位置
                    his_score_qp[i][j] = his_score

                    # 实际上还没落子，不能改变落子棋盘，需要还原落子棋盘
                    qp[i][j] = 0

        # 获取我方打分棋盘的最高分
        my_max_score = np.max(my_score_qp)
        # 获取对方打分棋盘的最高分
        his_max_score = np.max(his_score_qp)

        pos = []
        if my_max_score >= his_max_score:
            # 我方进攻，优先实现我方的最大连珠数
            my_pos = self.get_pos1(my_score_qp, my_max_score)
            # 获取对方在my_pos这些位置上的对大值
            his_score = self.get_max(his_score_qp, my_pos)
            # 获取对方最大值所在的所有位置，随机落子
            pos = self.get_pos2(his_score_qp, my_pos, his_score)
        else:
            # 我方防守，优先实现对方的最大连珠数
            his_pos = self.get_pos1(his_score_qp, his_max_score)
            # 获取对方在my_pos这些位置上的对大值
            my_score = self.get_max(my_score_qp, his_pos)
            # 获取对方最大值所在的所有位置，随机落子
            pos = self.get_pos2(my_score_qp, his_pos, my_score)
        return pos


myAI = AIPlayer(1)