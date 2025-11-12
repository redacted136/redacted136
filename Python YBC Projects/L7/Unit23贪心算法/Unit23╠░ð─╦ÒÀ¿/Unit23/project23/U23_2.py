total = 17
coins = [10, 5, 1]
count = 0
for c in coins:
    # 是否使用当前金币，如果使用则更新金币个数和兑换金额
    if total >= c:
        count = total // c + count
        total = total % c


    # 如果兑换金额为0，结束循环
    if total ==0:
        break

print(count)