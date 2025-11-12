# 定义函数A
def A(n):
    print(n)

    if n ==1:
        return
    A(n-1)
A(100)