from stack import Stack


# 定义函数 to_binary，实现十进制转二进制的功能
def to_binary(num):
    # 定义栈，记录余数
    s = Stack()
    # 循环除以二取余，余数进栈的过程
    while True:
        # 除2
        shang = num // 2
        # 取余
        yu = num % 2
        # 余数进栈
        s.push(yu)

        # 如果商为0，则转换完成。
        if shang == 0:
            break
        # 否则，商作为被除数继续进行运算
        else:
            num = shang