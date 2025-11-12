# 定义函数返回整数n的阶乘
def fn(n):
    # 增加终止条件
    if n == 1:
        return 1
    res = n *fn(n-1)
    return res
a = fn(6)
print(a)