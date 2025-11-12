class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度
# 生成实例：dog_1
dog_1 = Dog()
# 设置实例的攻击力为之前的2倍
dog_1.power *= 2
# 输出dog_1的攻击力
print(dog_1.power)


