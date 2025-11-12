from U3_game import start_game

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
        self.hp = self.hp + 3000
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
dog_1 = Dog()  # 生成实例：dog_1
start_game(dog_1) # 匹配对手monster（attack和heal随机出），开始战斗