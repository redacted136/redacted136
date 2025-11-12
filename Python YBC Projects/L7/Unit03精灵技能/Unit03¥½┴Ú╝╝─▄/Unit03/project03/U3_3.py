class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度
    def attack(self):
        # 设定技能威力为攻击力
        damage = self.power
        # 返回技能威力
        return damage

# 生成实例：dog_1
dog_1 = Dog()
# 实例使用attack函数
res = dog_1.attack()
print(res)



