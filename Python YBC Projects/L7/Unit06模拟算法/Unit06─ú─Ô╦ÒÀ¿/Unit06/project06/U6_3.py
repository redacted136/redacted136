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
    # 技能评分函数
    def give_point(self):
        jn = {'attack': 0, 'heal': 0, 'leech': 0, 'control': 0, 'attack_buff': 0,
              'defense_buff': 0}
        # 获取当前血量和最大血量的比值，即血量比
        rate = self.hp / self.max_hp
        # 给attack技能打分为100 * rate
        jn['attack'] = 100 * rate
        # 给attack技能打分为100 - attack技能的评分
        jn['heal'] = 100 - jn['attack']
        # 如果血量比rate大于0.5
        if rate > 0.5:
            # 给吸血技能评分，即给jn['leech']设置值为45 ~80之间的随机整数
            jn['leech'] = random.randint(45, 80)
        # 给控制技能评分，即给jn['control']设置值为45~55之间的随机整数
        jn['control'] = random.randint(45, 55)
        # 如果血量比rate大于0.8
        if rate > 0.8:
            # 给attack_buff技能设置值为80~100之间的随机整数
            jn['attack_buff'] = random.randint(80, 100)
            # 给defense_buff技能设置值为80~100之间的随机整数
            jn['defense_buff'] = random.randint(80, 100)
        # 返回技能评分字典jn
        return jn
    # 技能决策函数
    def decision(self):
        # 调用give_point函数,获取技能评分字典
        jn = self.give_point()
        # 初始化最高技能分，初始值为0
        max_point = 0
        # 初始化最高评分技能名，初始值为''
        max_jn = ''
        # 遍历技能字典
        for k in jn:
            # 如果技能评分大于最高技能分
            if jn[k] > max_point:
                # 记录最高分，即给max_point赋值为jn[k]
                max_point = jn[k]
                # 记录最高评分技能名，即给max_jn赋值为k
                max_jn = k
        # 返回评分最高技能名
        return max_jn


dog_1 = Dog('wanger', 0, 210, 110, 60, 6)
# 调用技能决策函数decision
res = dog_1.decision()
print(res)
