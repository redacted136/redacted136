class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度

    def attack(self):
        print('喷火')


dog_1 = Dog()  # 生成实例：dog_1
dog_1.attack()  # 实例使用attack函数


