def check_bound(a, i, j):
    if 0 <= i < a.shape[0]:
        if 0 <= j < a.shape[1]:
            return True
    else:
        return False

def get_sidepoint(qp, dir, step, left, right, hiscolor):
    left_color = 0
    right_color = 0
    if dir == 1:  # 横向
        # 如果left已经超出边界了，则left为[]
        if len(left) != 0:
            # check left of left 是否在棋盘范围内， 在则left_color赋值0/1/2
            if check_bound(qp, left[0], left[1] - step):
                left_color = qp[left[0]][left[1] - step]
            # 不在，则设置为阻挡
            else:
                left_color = hiscolor
        else:
            # 如果left为空，left of left也都设置为阻挡
            left_color = hiscolor
        if len(right) != 0:
            if check_bound(qp, right[0], right[1] + step):
                right_color = qp[right[0]][right[1] + step]
            else:
                right_color = hiscolor
        else:
            right_color = hiscolor

    elif dir == 2:  # 纵向
        if len(left) != 0:
            if check_bound(qp, left[0] - step, left[1]):
                left_color = qp[left[0] - step][left[1]]
            else:
                left_color = hiscolor
        else:
            left_color = hiscolor
        if len(right) != 0:
            if check_bound(qp, right[0] + step, right[1]):
                right_color = qp[right[0] + step][right[1]]
            else:
                right_color = hiscolor
        else:
            right_color = hiscolor

    elif dir == 3:  # 斜向1
        if len(left) != 0:
            if check_bound(qp, left[0] - step, left[1] - step):
                left_color = qp[left[0] - step][left[1] - step]
            else:
                left_color = hiscolor
        else:
            left_color = hiscolor
        if len(right) != 0:
            if check_bound(qp, right[0] + step, right[1] + step):
                right_color = qp[right[0] + step][right[1] + step]
            else:
                right_color = hiscolor
        else:
            right_color = hiscolor
    elif dir == 4:  # 斜向2
        if len(left) != 0:
            if check_bound(qp, left[0] + step, left[1] - step):
                left_color = qp[left[0] + step][left[1] - step]
            else:
                left_color = hiscolor
        else:
            left_color = hiscolor
        if len(right) != 0:
            if check_bound(qp, right[0] - step, right[1] + step):
                right_color = qp[right[0] - step][right[1] + step]
            else:
                left_color = hiscolor
        else:
            right_color = hiscolor

    return [left_color, right_color]


def pattern(qp, dir, count, mycolor, right, rightcolor, left, leftcolor):
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
        side = get_sidepoint(qp, dir, 1, left, right, hiscolor)
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
        side1 = get_sidepoint(qp, dir, 1, left, right, hiscolor)
        left_color = side1[0]
        right_color = side1[1]
        side2 = get_sidepoint(qp, dir, 2, left, right, hiscolor)
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
        side1 = get_sidepoint(qp, dir, 1, left, right, hiscolor)
        left_color = side1[0]
        right_color = side1[1]
        side2 = get_sidepoint(qp, dir, 2, left, right, hiscolor)
        left__color = side2[0]
        right__color = side2[1]
        side3 = get_sidepoint(qp, dir, 3, left, right, hiscolor)
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


def score(p1, p2, p3, p4):
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