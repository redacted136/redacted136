from stack import Stack

s = Stack()
for i in range(1, 7):
    s.push('网址' + str(i))
for o in range(1, 7):
    # 当栈顶为网址3时，结束循环，否则出栈
    if s.peek() == '网址3':
    break
else:
    s.pop()



print(s.peek())
