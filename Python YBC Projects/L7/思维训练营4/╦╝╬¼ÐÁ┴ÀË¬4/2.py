list1 = [1, 2, 1, 2, 4, 2, 6, 5, 5, 5, 6, 1]
set1 = set(list1)
print(set1)

list2 = [1, 2, 3, 2, 1, 1, 4, 1, 1, 2, 1, 3]
# 把列表转换成集合，实现去重
# 输出2班奖品结果
set2 = set(list2)
print(set2)
# set1和set2的交集
# 输出结果
set3 = set1&set2
print(set3)
