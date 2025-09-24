from stack import Stack


# 定义函数 isMatch 判断字符串 st 中的括号是否匹配
def isMatch(st):
    # 定义一个栈，记录待配对
    s = Stack()
    # 定义一个字典来储存左右括号的匹配关系
    kh = {')': '(', ']': '[', '}': '{'}
    # 遍历字符串st
    for char in st:
        # 如果字符char为左括号，则字符char入栈
        if char in '([{':
            s.push(char)
        # 否则（遇到右括号）
        else:
            # 如果与栈顶元素配对成功，则左括号出栈
            if s.peek() == kh[char]:
                s.pop()
            # 否则，表示匹配失败，返回错误
            else:
                return False

    # 遍历完字符串后，如果栈为空，则表示全部括号匹配成功
    if s.size() == 0:
        return True

# 调用 isMatch 函数对字符串 '{[()()]}' 进行括号匹配判断
print(isMatch('{[()()]}'))