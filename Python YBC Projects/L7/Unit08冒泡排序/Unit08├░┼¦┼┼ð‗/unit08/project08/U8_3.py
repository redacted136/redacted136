lst = [15, 11, 9, 6, 3]
# 循环四次
for r in range(len(lst)-1):
    # 确定未排序部分范围
    for i in range(len(lst)-r-1):
        # 比较相邻元素
        # 如果前一个元素比后一个元素大， 则交换元素位置
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

    print(lst)
