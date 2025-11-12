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
        name = []
        point = []
        for key in jn:
            name.append(key)
            point.append(jn[key])
        for r in range(len(point)-1):
            max_i = r
            for i in range(r+1, len(point)):
                if point[i] > point[max_i]:
                    max_i = i
            point[max_i], point[r] = point[r], point[max_i]
            name[max_i], name[r] = name[r], name[max_i]
            print(name)
            print(point)

dog_2 = Dog('WangEr', 0, 1200, 1000, 400, 400)
dog_2.decision()
