lst = [3, 6, 11, 9, 15]
# 循环四次
for r in range(len(lst)-1):
    print('第' + str(r+1) + '次循环')
    # 确定未排序部分范围
    for i in range(len(lst)-r):
        print('未排序元素索引：' + str(i))