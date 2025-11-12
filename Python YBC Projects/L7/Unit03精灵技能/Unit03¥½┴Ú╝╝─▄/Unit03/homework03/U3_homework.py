# 壮猿想设计一个飞机类，请大家一起来帮助他！
# 为Plane类创建一个jia_su函数，在函数中设定属性速度(speed)为之前的2倍
# 为Plane类创建一个jian_su函数，在函数中设定属性速度(speed)为之前的0.5倍

# 创建一个飞机类(Plane)
class Plane():
    # 添加属性——型号
    type = 'A320'
    # 添加属性——速度
    speed = 200
    # 创建一个jia_su函数，在函数中设定属性速度(speed)为之前的2倍

    def jia_su(self):
        s1 = self.speed * 2
        return s1

    #创建一个jian_su函数，在函数中设定属性速度(speed)为之前的0.5倍
    def jian_su(self):
        s2 = self.speed * 0.5
        return s2
#生成实例：plane1


plane1 = Plane()
#生成实例：plane2


plane2 = Plane()
#实例plane1使用jia_su函数，输出速度


res1 = plane1.jia_su()
print(res1)

#实例plane2使用jian_su函数，输出速度
res2 = plane2.jian_su()
print(res2)
