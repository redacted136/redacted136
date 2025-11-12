from game import start_game


def check(qp, i_next, j_next):
    if 0 <= i_next <= qp.shape[0]-1:
        if 0 <= j_next <= qp.shape[1]-1:
            return True
    else:
        return False


def check_victory(qp, i, j):
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
    if count1 >= 5:
        return True
    # 继续判断竖向、斜向1、斜向2是否五子连珠
    elif count2 >= 5:
    elif count3 >= 5:
    elif count4 >= 5:
    else:
        return False

start_game(check_victory)


