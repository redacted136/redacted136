#遍历晴天数量的枚举范围
for sunny in range(9):
    #获取雨天的数量
    rainy = 8 - sunny
    #判定是否符合条件，如果符合，输出二者的数量
    if 20 * sunny + 12 * rainy == 112:
        print('晴天的数量:'+str(sunny))
        print('雨天的数量:'+str(rainy))