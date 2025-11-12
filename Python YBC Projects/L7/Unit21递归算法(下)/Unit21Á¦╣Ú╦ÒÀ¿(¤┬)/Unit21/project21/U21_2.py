# 100个人围成一圈，每个人对应的编号是1~100。然后从第一个人开始报数(从1到2)，如果报到2的人则退出游戏。
# 问：编号为几能留到最后。
# 注：每次报数都要从1开始，2截止。这也就意味着如果一圈的队尾报的数为1，那么要以队首报2截止。
# 创建空列表存储1~100人员编号
lis = []
for i in range(1,1001):
    lis.append(i)


# 定义函数函数获取最终人员编号
def get_num(lis):
    # 创建空列表存储每轮留下来的人
    newLis = []
    for i in range(len(lis)):
        if i % 2 == 0:
            newLis.append(lis[i])
    if len(lis) % 2 == 1:
        newLis.pop(0)
    if len(newLis) == 1:
        return newLis[0]
    return get_num(newLis)

# 打印结果
print(get_num(lis))