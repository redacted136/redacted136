from matplotlib import pyplot

# 将数据与标签按顺序存入两个列表中。
x = [163, 163, 165, 165, 166, 167, 168, 168, 169, 170, 170, 171, 172, 175, 176, 176, 177, 178]
y = [168, 170, 172, 168, 170, 172, 175, 173, 175, 178, 176, 175, 180, 182, 180, 185, 186, 183]

# 使用pyplot.scatter()函数绘制点。
pyplot.scatter(x, y)
# 使用pyplot.xlabel()函数为横轴命名。
pyplot.xlabel('father')
# 使用pyplot.ylabel()函数为纵轴命名。
pyplot.ylabel('child')
# 使用pyplot.show()函数显示所绘制的图。
pyplot.show()

pyplot.color('green')
pyplot.length(5)

