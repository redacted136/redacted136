# 从stack模块中导入Stack类
from stack import Stack

# 创建一个栈
s = Stack()

s.push('熊猫')
s.push('绵羊')
print(s.pop())
print(s.peek())
print(s.size())