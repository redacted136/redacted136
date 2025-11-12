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
dog_2 = Dog('WongEr', 0, 210.50, 40, 2,7)
# 输出实例dog_2的名字、攻击力、当前血量
print(dog_2.name, dog_2.power, dog_2.hp)
