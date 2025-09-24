class Stack():
    # 初始化实例属性
    def __init__(self):
        self.items = []
    # 定义函数实现入栈
    def push(self,item):
        return self.items.append(item)
    # 定义函数实现出栈
    def pop(self):
        return self.items.pop()

    # 定义函数：查看栈顶元素
    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]



# 定义函数：获取栈中元素的个数
def

















