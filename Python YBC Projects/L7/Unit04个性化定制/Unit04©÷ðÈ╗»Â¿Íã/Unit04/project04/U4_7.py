from U4_game import show_attr

class Dog():
    def __init__(self, n, t, m, p, d, s):
        self.name = n
        self.type = t
        self.max_hp = m
        self.power = p
        self.defense = d
        self.speed = s
        self.hp = self.max_hp
# 生成实例dog_2，初始化该实例属性


dog_2 = Dog('WangEr',0, 210 ,110 ,60 ,6)
# 生成实例dog_7，初始化该实例属性
dog_7 = Dog('WangQi',1,300,90,55,7)
# 显示实例及其属性
show_attr(dog_2,dog_7)