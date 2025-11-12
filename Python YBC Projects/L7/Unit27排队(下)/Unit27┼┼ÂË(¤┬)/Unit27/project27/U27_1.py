from queue import Queue


lst = [5, 6, 2, 1, 3, 4]
max_l = Queue()
max_l.put(lst[0])
# 从第二个元素开始，遍历列表
for i in range(1, len(lst)):
    # max_l中的元素出队
    num = max_l.get()
    # 与遍历的元素做比较
    if list[i]> num:
        max_l.put(lst[i])
    else:
        max_l.put(num)

print(max_l.get())