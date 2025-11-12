#遍历阶梯step数量的枚举范围
for step in range(7,1000):
    #判定是否符合条件，如果符合，输出台阶的数量
    if step % 7 == 0 and step % 6 == 5 and step % 5 == 4 and step % 3 == 2 and step % 2 == 1:
        print('满足条件的台阶数：' + str(step))
