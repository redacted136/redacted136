# AI竞技平台：https://www.yuanfudao.com/ada-heracles/index.html#/ai
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

    # 攻击强化技能
    def attack_buff(self):
        self.power = self.power * 1.05

    # 防御强化技能
    def defense_buff(self):
        self.defense = self.defense * 1.05

    # 技能评分函数
    def give_point(self):
        jn = {'attack': 0, 'heal': 0, 'leech': 0, 'control': 0, 'attack_buff': 0,
              'defense_buff': 0}
        rate = self.hp / self.max_hp
        jn['attack'] = 100 * rate
        jn['heal'] = 100 - jn['attack']
        if rate > 0.5:
            jn['leech'] = random.randint(45, 80)
        jn['control'] = random.randint(45, 55)
        if rate > 0.8:
            jn['attack_buff'] = random.randint(80, 100)
            jn['defense_buff'] = random.randint(80, 100)
        return jn

    # 技能决策函数(出招函数)
    def decision(self):
        jn = self.give_point()
        max_point = 0
        max_jn = ''
        for k in jn:
            if jn[k] > max_point:
                max_point = jn[k]
                max_jn = k
        return max_jn


# 创建Dog实例，并赋值为my_monster变量(属性之和不超过3000)
my_monster = Dog('REDACTED', 1, 1300, 1000, 500, 200)
