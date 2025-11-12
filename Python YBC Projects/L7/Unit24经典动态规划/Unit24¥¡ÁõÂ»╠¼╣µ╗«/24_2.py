B = [0, 0, 0]
weight = [3, 4, 5]
value = [4, 5, 6]
for n in range(3, 11):
    lst = []
    # 依次尝试书包承重为n时，是否能装入1号、2号、3号礼品
    for i in range(0, 3):
        # 如果能装入该礼品，则计算出该方案包中礼品的价值
        if n >= weight[i]:
            lst.append( value[i] + B[n-weight[i]])
    B.append(max(lst))
print(B[10])
