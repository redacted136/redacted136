lst = [9, 15, 3, 11, 6]
# 循环4次
for r in range(len(lst) - 1):
    # 定义一个变量max_i, 记录当前最大值的索引
    # max_i初始值定义为未排序列表的第一个索引：r
    max_i = r
    # 在未排序部分寻找最大值
    for i in range(r+1, len(lst)):
        if lst[i] > lst[max_i]:
            max_i = i
    # 找到最大值后与未排序部分的第一项交换位置



    print(max_i)
    print(lst)