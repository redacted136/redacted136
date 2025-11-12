import random


# 定义Dog类
class Dog():
    def __init__(self, n, t, m, p, d, s):
        self.name = n
        self.type = t
        self.max_hp = m
        self.power = p
        self.defense = d
        self.speed = s
        self.hp = self.max_hp
    # 攻击技能
    def attack(self):
        damage = self.power
        return damage
    # 治疗技能
    def heal(self):
        hp_up = self.max_hp * 0.6
        self.hp = self.hp + hp_up
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
    # 吸血技能
    def leech(self):
        damage = self.power * 0.6
        hp_up = damage * 0.5
        self.hp = self.hp + hp_up
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        return damage
    # 控制技能
    def control(self):
        lis1 = [1, 0]
        x = random.choice(lis1)
        if x == 1:
            return True
        else:
            return False
    # 攻击增强技能
    def attack_buff(self):
        self.power = self.power * 1.05
    # 防御增强技能
    def defense_buff(self):
        self.defense = self.defense * 1.05
    # 技能筛选函数
    def give_point(self):
        jn = {'attack': 0, 'heal': 0, 'leech': 0, 'control': 0, 'attack_buff': 0,
              'defense_buff': 0}
        # 定义变量rate,值为当前血量占最大血量的比例
        rate = self.hp / self.max_hp
        # 如果血量比rate大于0.8
        if rate > 0.8:
            # 给攻击技能打分
            jn['attack'] = 100
        elif rate > 0.5:
            # 给控制技能打分
            jn['control'] = 100
        elif rate > 0.3:
            # 给攻击增强技能打分
            jn['attack_buff'] = 100
        else:
            # 给治疗技能打分
            jn['heal'] = 100
        # 返回技能评分字典jn
        return jn





dog_1 = Dog('wanger', 0, 800, 110, 60, 6)
# dog_1使用give_point函数获取技能评分字典，结果保存到jn中。
jn = dog_1.give_point()
print(jn)
