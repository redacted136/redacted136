import random


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
        self.hp = self.hp + hp_up
        if self.hp >= self.max_hp:
            self.hp = self.max_hp  # hp上限为max_hp
        return damage

    # 创建控制函数
    def control(self):
        lis1 = [1, 0]
        # 获取列表中随机一个元素
        x = random.choice(lis1)
        # 命中,停止行动两回合
        if x == 1:
            return True
        else:
            return False

    # 创建攻击增强函数
    def attack_buff(self):
        self.power = self.power * 1.05

   # 创建防御增强函数
    def defense_buff(self):
        # 提升自身5%的防御力
        self.defense = self.defense * 1.05

dog_2 = Dog('WangEr',0,210,110,60,6)
dog_2.defense_buff() # 实例使用defense_buff函数
print(dog_2.defense)
