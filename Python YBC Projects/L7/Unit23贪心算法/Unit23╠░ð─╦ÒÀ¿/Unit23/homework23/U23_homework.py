total = 36
coins = [10, 5, 1]
count = 0
for c in coins:
    # 是否使用当前金币，如果使用则更新金币个数和兑换金额
    if total >= c:
        count = total // c + count
        total = total % c

    if total == 0:
        break
print(count)
