class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度
dog_1 = Dog()  #生成实例：dog_1
dog_2 = Dog()  #生成实例：dog_2
dog_3 = Dog()  #生成实例：dog_3
print(dog_1.name) #输出dog_1的属性name
print(dog_2.name) #输出dog_2的属性name
print(dog_3.name) #输出dog_3的属性name


