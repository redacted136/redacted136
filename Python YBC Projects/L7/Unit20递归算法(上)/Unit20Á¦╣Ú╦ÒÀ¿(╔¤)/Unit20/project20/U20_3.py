# 定义函数计算n级台阶的迈法
def f(n):
    # 台阶数为1时，只有1种情况
    if n == 1:
        return 1
    # 台阶数为2时，只有两种情况
    if n == 2:
        return 2
    res = f(n-2) + f(n-1)
    return res

print(f(50))