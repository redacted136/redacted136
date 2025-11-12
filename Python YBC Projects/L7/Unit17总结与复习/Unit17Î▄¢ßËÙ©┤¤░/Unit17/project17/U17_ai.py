import numpy as np
import random

class AIPlayer():
    def __init__(self, clr):
        self.color = clr  # black:1, white:2

    def check_bound(self, a, i, j):
        if 0 <= i < a.shape[0]:
            if 0 <= j < a.shape[1]:
                return True
        else:
            return False

    def get_sidepoint(self, qp, dir, step, left, right, hiscolor):
        left_color = 0
        right_color = 0
        if dir == 1:  # 横向
            # 如果left已经超出边界了，则left为[]
            if len(left) != 0:
                # check left of left 是否在棋盘范围内， 在则left_color赋值0/1/2
                if self.check_bound(qp, left[0], left[1] - step):
                    left_color = qp[left[0]][left[1] - step]
                # 不在，则设置为阻挡
                else:
                    left_color = hiscolor
            else:
                # 如果left为空，left of left也都设置为阻挡
                left_color = hiscolor
            if len(right) != 0:
                if self.check_bound(qp, right[0], right[1] + step):
                    right_color = qp[right[0]][right[1] + step]
                else:
                    right_color = hiscolor
            else:
                right_color = hiscolor

        elif dir == 2:  # 纵向
            if len(left) != 0:
                if self.check_bound(qp, left[0] - step, left[1]):
                    left_color = qp[left[0] - step][left[1]]
                else:
                    left_color = hiscolor
            else:
                left_color = hiscolor
            if len(right) != 0:
                if self.check_bound(qp, right[0] + step, right[1]):
                    right_color = qp[right[0] + step][right[1]]
                else:
                    right_color = hiscolor
            else:
                right_color = hiscolor

        elif dir == 3:  # 斜向1
            if len(left) != 0:
                if self.check_bound(qp, left[0] - step, left[1] - step):
                    left_color = qp[left[0] - step][left[1] - step]
                else:
                    left_color = hiscolor
            else:
                left_color = hiscolor
            if len(right) != 0:
                if self.check_bound(qp, right[0] + step, right[1] + step):
                    right_color = qp[right[0] + step][right[1] + step]
                else:
                    right_color = hiscolor
            else:
                right_color = hiscolor
        elif dir == 4:  # 斜向2
            if len(left) != 0:
                if self.check_bound(qp, left[0] + step, left[1] - step):
                    left_color = qp[left[0] + step][left[1] - step]
                else:
                    left_color = hiscolor
            else:
                left_color = hiscolor
            if len(right) != 0:
                if self.check_bound(qp, right[0] - step, right[1] + step):
                    right_color = qp[right[0] - step][right[1] + step]
                else:
                    left_color = hiscolor
            else:
                right_color = hiscolor

        return [left_color, right_color]

    def pattern(self, qp, dir, count, mycolor, right, rightcolor, left, leftcolor):
        # 判断当前连珠数我方棋子颜色和对方棋子颜色
        hiscolor = 0
        if mycolor == 1:
            hiscolor = 2
        else:
            hiscolor = 1

        if count >= 5:
            return 'WIN5'

        elif count == 4:
            if leftcolor == 0 and rightcolor == 0:
                return 'ALIVE4'
            elif leftcolor == 0 or rightcolor == 0:
                return 'DIE4'
            elif leftcolor == hiscolor and rightcolor == hiscolor:
                return 'NOTHING'

        elif count == 3:
            side = self.get_sidepoint(qp, dir, 1, left, right, hiscolor)
            left_color = side[0]
            right_color = side[1]

            if leftcolor == 0 and rightcolor == 0:
                if left_color == hiscolor and right_color == hiscolor:
                    return 'DIE3'
                elif left_color == mycolor or right_color == mycolor:
                    return 'LOW_DIE4'
                elif left_color == 0 or right_color == 0:
                    return 'ALIVE3'
            elif leftcolor == hiscolor and rightcolor == hiscolor:
                return 'NOTHING'
            elif leftcolor == 0 or right_color == 0:
                if leftcolor == hiscolor:
                    if right_color == hiscolor:
                        return 'NOTHING'
                    elif right_color == 0:
                        return 'DIE3'
                    elif right_color == mycolor:
                        return 'LOW_DIE4'
                elif rightcolor == hiscolor:
                    if left_color == hiscolor:
                        return 'NOTHING'
                    elif left_color == 0:
                        return 'DIE3'
                    elif left_color == mycolor:
                        return 'LOW_DIE4'

        elif count == 2:
            side1 = self.get_sidepoint(qp, dir, 1, left, right, hiscolor)
            left_color = side1[0]
            right_color = side1[1]
            side2 = self.get_sidepoint(qp, dir, 2, left, right, hiscolor)
            left__color = side2[0]
            right__color = side2[1]

            if leftcolor == 0 and rightcolor == 0:
                if (right_color == 0 and right__color == mycolor) \
                        or (left_color == 0 and left__color == mycolor) \
                        or (right_color == mycolor and right__color == hiscolor) \
                        or (left_color == mycolor and left__color == hiscolor):
                    return 'DIE3'
                elif left_color == 0 and right_color == 0:
                    return 'ALIVE2'
                elif (right_color == mycolor and right__color == mycolor) \
                        or (left_color == mycolor and left__color == mycolor):
                    return 'LOW_DIE4'
                elif (right_color == mycolor and right__color == 0) \
                        or (left_color == mycolor and left__color == 0):
                    return 'TIAO3'
            elif leftcolor == hiscolor and rightcolor == hiscolor:
                return 'NOTHING'
            elif leftcolor == 0 or rightcolor == 0:
                if leftcolor == hiscolor:
                    if right_color == hiscolor or right__color == hiscolor:
                        return 'NOTHING'
                    elif right_color == 0 and right__color == 0:
                        return 'DIE2'
                    elif right_color == mycolor and right__color == mycolor:
                        return 'LOW_DIE4'
                    elif right_color == mycolor or right__color == mycolor:
                        return 'DIE3'
                elif rightcolor == hiscolor:
                    if left_color == hiscolor or left__color == hiscolor:
                        return 'NOTHING'
                    elif left_color == 0 and left__color == 0:
                        return 'DIE2'
                    elif left_color == mycolor and left__color == mycolor:
                        return 'LOW_DIE4'
                    elif left_color == mycolor or left__color == mycolor:
                        return 'DIE3'

        elif count == 1:
            side1 = self.get_sidepoint(qp, dir, 1, left, right, hiscolor)
            left_color = side1[0]
            right_color = side1[1]
            side2 = self.get_sidepoint(qp, dir, 2, left, right, hiscolor)
            left__color = side2[0]
            right__color = side2[1]
            side3 = self.get_sidepoint(qp, dir, 3, left, right, hiscolor)
            left___color = side3[0]
            right___color = side3[1]

            if leftcolor == 0 and left_color == mycolor and left__color == mycolor and left___color == mycolor:
                return 'LOW_DIE4'
            elif rightcolor == 0 and right_color == mycolor and right__color == mycolor and right___color == mycolor:
                return 'LOW_DIE4'

            elif leftcolor == 0 and left_color == mycolor and left__color == mycolor and left___color == hiscolor and rightcolor == 0:
                return 'DIE3'
            elif rightcolor == 0 and right_color == mycolor and right__color == mycolor and right___color == hiscolor and leftcolor == 0:
                return 'DIE3'

            elif leftcolor == 0 and left_color == mycolor and left__color == mycolor and left___color == 0 and rightcolor == 0:
                return 'TIAO3'
            elif rightcolor == 0 and right_color == mycolor and right__color == mycolor and right___color == 0 and leftcolor == 0:
                return 'TIAO3'

            elif leftcolor == 0 and left_color == 0 and left__color == mycolor and left___color == mycolor:
                return 'DIE3'
            elif rightcolor == 0 and right_color == 0 and right__color == mycolor and right___color == mycolor:
                return 'DIE3'

            elif leftcolor == 0 and left_color == mycolor and left__color == 0 and left___color == mycolor:
                return 'DIE3'
            elif rightcolor == 0 and right_color == mycolor and right__color == 0 and right___color == mycolor:
                return 'DIE3'

            elif leftcolor == 0 and left_color == mycolor and left__color == 0 and left___color == 0 and rightcolor == 0:
                return 'LOW_ALIVE2'
            elif rightcolor == 0 and right_color == mycolor and right__color == 0 and right___color == 0 and leftcolor == 0:
                return 'LOW_ALIVE2'

            elif leftcolor == 0 and left_color == 0 and left__color == mycolor and left___color == 0 and rightcolor == 0:
                return 'LOW_ALIVE2'
            elif rightcolor == 0 and right_color == 0 and right__color == mycolor and right___color == 0 and leftcolor == 0:
                return 'LOW_ALIVE2'
        return 'NOTHING'

    def score(self, p1, p2, p3, p4):
        pattern_lst = [p1, p2, p3, p4]

        win5 = 0

        alive4 = 0
        die4 = 0
        lowdie4 = 0

        alive3 = 0
        tiao3 = 0
        die3 = 0

        alive2 = 0
        lowalive2 = 0
        die2 = 0

        nothing = 0

        for p in pattern_lst:
            if p == 'WIN5':
                win5 += 1
            elif p == 'ALIVE4':
                alive4 += 1
            elif p == 'DIE4':
                die4 += 1
            elif p == 'LOW_DIE4':
                lowdie4 += 1
            elif p == 'ALIVE3':
                alive3 += 1
            elif p == 'TIAO3':
                tiao3 += 1
            elif p == 'DIE3':
                die3 += 1
            elif p == 'ALIVE2':
                alive2 += 1
            elif p == 'LOW_ALIVE2':
                lowalive2 += 1
            elif p == 'DIE2':
                die2 += 1
            elif p == 'NOTHING':
                nothing += 1

        die4_ = die4 + lowdie4
        alive3_ = alive3 + tiao3
        alive2_ = alive2 + lowalive2

        if win5 >= 1:
            return 100000
        elif alive4 >= 1 or die4_ >= 2 or (die4_ >= 1 and alive3_ >= 1):
            return 10000
        elif alive3_ >= 2:
            return 5000
        elif die3 >= 1 and alive3 >= 1:
            return 1000
        elif die4 >= 1:
            return 500
        elif alive3 >= 1:
            return 400
        elif tiao3 >= 1:
            return 100
        elif alive2_ >= 2:
            return 90
        elif alive2 >= 1:
            return 50
        elif lowalive2 >= 1:
            return 10
        elif die3 >= 1:
            return 5
        elif die2 >= 1:
            return 2
        else:
            return 1

    # 数组边界判定
    def check(self, qp, i_next, j_next):
        if 0 <= i_next <= qp.shape[0] - 1:
            if 0 <= j_next <= qp.shape[1] - 1:
                return True
        else:
            return False

    # 获取4个方向连珠数的最大值
    def get_score(self, qp, i, j):
        if qp[i][j] == 1:
            hiscolor = 2
        else:
            hiscolor = 1

        # 统计横向连珠数count1
        count1 = 1
        dir1 = []
        color1 = 0
        for step in range(1, 5):
            i_next = i
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count1 += 1
                else:
                    dir1 = [i_next, j_next]
                    color1 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color1 = hiscolor
                break
        dir2 = []
        color2 = 0
        for step in range(1, 5):
            i_next = i
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count1 += 1
                else:
                    dir2 = [i_next, j_next]
                    color2 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color2 = hiscolor
                break
        p1 = self.pattern(qp, 1, count1, qp[i][j], dir1, color1, dir2, color2)

        # 统计纵向连珠数count2
        count2 = 1
        dir3 = []
        color3 = 0
        for step in range(1, 5):
            i_next = i + step
            j_next = j
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count2 += 1
                else:
                    dir3 = [i_next, j_next]
                    color3 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color3 = hiscolor
                break
        dir4 = []
        color4 = 0
        for step in range(1, 5):
            i_next = i - step
            j_next = j
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count2 += 1
                else:
                    dir4 = [i_next, j_next]
                    color4 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color4 = hiscolor
                break
        p2 = self.pattern(qp, 2, count2, qp[i][j], dir3, color3, dir4, color4)

        # 统计斜向1连珠数count3
        count3 = 1
        dir5 = []
        color5 = 0
        for step in range(1, 5):
            i_next = i + step
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count3 += 1
                else:
                    dir5 = [i_next, j_next]
                    color5 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color5 = hiscolor
                break
        dir6 = []
        color6 = 0
        for step in range(1, 5):
            i_next = i - step
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count3 += 1
                else:
                    dir6 = [i_next, j_next]
                    color6 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color6 = hiscolor
                break
        p3 = self.pattern(qp, 3, count3, qp[i][j], dir5, color5, dir6, color6)

        # 统计斜向2连珠数count4
        count4 = 1
        dir7 = []
        color7 = 0
        for step in range(1, 5):
            i_next = i - step
            j_next = j + step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count4 += 1
                else:
                    dir7 = [i_next, j_next]
                    color7 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color7 = hiscolor
                break
        dir8 = []
        color8 = 0
        for step in range(1, 5):
            i_next = i + step
            j_next = j - step
            if self.check(qp, i_next, j_next):
                if qp[i_next][j_next] == qp[i][j]:
                    count4 += 1
                else:
                    dir8 = [i_next, j_next]
                    color8 = qp[i_next][j_next]
                    break
            else:
                # 超出边界，算为阻挡
                color8 = hiscolor
                break
        p4 = self.pattern(qp, 4, count4, qp[i][j], dir7, color7, dir8, color8)

        # 根据落子位置四个方向上的棋型，为当前位置打分
        p_score = self.score(p1, p2, p3, p4)
        return p_score

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

        if my_max_score >= his_max_score:
            # 我方进攻
            # 获取我方打分棋盘最高分对应的所有位置
            my_pos = self.get_pos1(my_score_qp, my_max_score)
            # 获取对方在my_pos这些位置上的最大值
            his_score = self.get_max(his_score_qp, my_pos)
            # 获取对方最大值所在的所有位置，随机落子
            pos = self.get_pos2(his_score_qp, my_pos, his_score)
        else:
            # 我方防守
            # 获取对方打分棋盘最高分对应的所有位置
            his_pos = self.get_pos1(his_score_qp, his_max_score)
            #  获取我方在his_max_pos这些位置上的最大值
            my_score = self.get_max(my_score_qp, his_pos)
            # 获取我方最大值所在的所有位置，随机落子
            pos = self.get_pos2(my_score_qp, his_pos, my_score)
        return pos


myAI = AIPlayer(1)