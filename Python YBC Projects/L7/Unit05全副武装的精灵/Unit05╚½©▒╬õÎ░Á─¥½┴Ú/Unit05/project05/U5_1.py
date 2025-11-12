class Dog():
    # 初始化实例属性
    def __init__(self, n, t, m, p, d, s):
        self.name = n
        self.type = t
        self.max_hp = m
        self.power = p
        self.defense = d
        self.speed = s
        self.hp = self.max_hp

    # 创建攻击函数
    def attack(self):
        damage = self.power
        return damage

    # 创建治疗函数
    def heal(self):
        hp_up = self.max_hp * 0.6
        self.hp = self.hp + hp_up
        if self.hp >= self.max_hp:
            self.hp = self.max_hp

    # 创建吸血函数
    def leech(self):
        # 攻击威力为攻击力的60%
        damage = self.power * 0.6
        # 回血量为攻击威力的50%
        hp_up = damage * 0.5
        # 在当前血量的基础上加回血量
        self.hp = hp_up + self.hp
        if self.hp >= self.max_hp:
            self.hp = self.max_hp  # hp上限为max_hp
        return damage


dog_2 = Dog('WangEr',0,210,110,60,6)
res = dog_2.leech() # 210*0.6 = 66
print(res)
