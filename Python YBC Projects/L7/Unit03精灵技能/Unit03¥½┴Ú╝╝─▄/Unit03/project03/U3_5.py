class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度
    def attack(self):
        # 设定技能威力为攻击力的2倍
        damage = self.power * 2
        return damage
dog_1 = Dog() # 生成实例：dog_1
# 实例使用attack函数
res = dog_1.attack()
print(res)



