class Dog():
    def set_attr(self, n, t, m, p, d, s):
        self.name = n
        self.type = t
        self.max_hp = m
        self.power = p
        self.defense = d
        self.speed = s
        self.hp = self.max_hp
dog_2 = Dog() # 生成实例dog_2
# 使用set_attr函数传递实例dog_2的属性值
dog_2.set_attr('WangEr',0,2000,60,60,6)
# 输出实例dog_2的名字、攻击力、当前血量
print(dog_2.name,dog_2.power,dog_2.hp)
