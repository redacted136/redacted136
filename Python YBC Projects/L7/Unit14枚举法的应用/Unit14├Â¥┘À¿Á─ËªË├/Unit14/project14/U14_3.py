#遍历晴天sunny数量的枚举范围
for sunny in range(6):
    #获取雨天rainy的数量
    rainy = 8 - sunny
    #判定是否符合条件，如果符合，输出二者的数量
    if sunny * 20 + rainy * 12 == 112:
        print('晴天的数量:'+str(sunny))
        print('雨天的数量:'+str(rainy))
        break