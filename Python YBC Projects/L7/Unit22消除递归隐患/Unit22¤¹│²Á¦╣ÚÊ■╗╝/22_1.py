def f(n):
    # 终止条件
    if n == 1:
        return 1
    if n == 2:
        return 2
    res = f(n-1) + f(n-2)
    return res
print(f(100))