class Dog():
    name = 'WangDa'  # 名字
    type = 0  # 角色属性
    max_hp = 2000  # 最大血量
    hp = max_hp  # 当前血量
    power = 999  # 攻击力
    defense = 999  # 防御力
    speed = 999  # 速度

    def attack(self):
        damage = self.power
        return damage

    def heal(self):
        # 每次回血3000
        self.hp += 3000
        # 当前血量上限为max_hp
        if self.hp >= self.max_hp:
            self.hp = self.max_hp


dog_1 = Dog()  # 成实例：dog_1
dog_1.heal() # 实例使用heal函数
print(dog_1.hp)