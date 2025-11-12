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
        # 横向向左判断，行索引i值不变，列索引j值减小
        i_next = i
        j_next = j - step
        if check(qp, i_next, j_next):
            # 判断下一个位置的棋子是否与新落棋子同色，如果同色count1加1
            if qp[i_next][j_next] == qp[i][j]:
                count1 += 1
            else:
                break

    if count1 >= 5:
        return True
    else:
        return False

start_game(check_victory)


