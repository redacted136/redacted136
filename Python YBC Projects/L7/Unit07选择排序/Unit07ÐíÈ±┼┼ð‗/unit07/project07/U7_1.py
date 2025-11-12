from U7_game import start_game
import random

class Dog():
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
        damage = self.power * 0.6  # 技能威力为攻击力的60%
        hp_up = damage * 0.5  # 回血量为技能威力的50%
        self.hp = self.hp + hp_up  # 在当前血量的基础上加回血量
        if self.hp >= self.max_hp:
            self.hp = self.max_hp  # hp上限为max_hp
        return damage

    # 创建控制函数
    def control(self):
        lis1 = [1,0]
        x = random.choice(lis1)
        if x == 1: # 命中停止行动两回合
            return True
        else:
            return False

    # 创建攻击增强函数
    def attack_buff(self):
        self.power = self.power * 1.05

    # 创建防御增强函数
    def defense_buff(self):
        self.defense = self.defense * 1.05

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

    def decision(self):
        jn = self.give_point()
        jn_l = []
        i = 3
        while i > 0:
            max_point = -1
            max_jn = ''
            for k in jn:
                if jn[k] >= max_point:
                    max_point = jn[k]
                    max_jn = k
            jn_l.append(max_jn)
            jn.pop(max_jn)
            i = i-1
        return jn_l

dog_2 = Dog('WangEr', 0, 1200, 1000, 400, 400)
start_game(dog_2)