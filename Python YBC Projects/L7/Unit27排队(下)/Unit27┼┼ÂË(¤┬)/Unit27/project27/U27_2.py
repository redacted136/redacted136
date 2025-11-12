from queue import Queue


lst = [5, 6, 2, 1, 3, 4]

# 应用队列的特点获取列表的最大值
def find_max(lst):
    max_l = Queue()
    max_l.put(three[0])
    # 从第二个元素开始，遍历列表
    for i in range(1, len(three)):
        # max_l中的元素出队
        num = max_l.get()
        # 与遍历的元素做比较
        if three[i] > num:
            max_l.put(three[i])
        else:
            max_l.put(num)
    return max_l.get()

# 定义一个列表来储存每三个相邻元素
three = []
# 遍历列表
for i in range(len(lst)):
    # 将元素添加到列表three中
    three.append(lst[i])
    # 保证列表中只有三个元素
    if len(three) ==4:
        three.pop(0)

    # 获取列表three的最大值
    if i >= 2:
        print(find_max(three))