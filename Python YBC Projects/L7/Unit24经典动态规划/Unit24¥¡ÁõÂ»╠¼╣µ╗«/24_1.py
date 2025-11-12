T = [0]
coins = [5, 4, 1]
for n in range(1, 189):
    lst = []
    # 依次尝试5、4、1元面值硬币
    for c in coins:
        # 如果能使用该面值金币，则存储计算结果
        if i >= c:
            lst.append(1 + T[n-c])
    T.append(min(lst))
print(T[188])