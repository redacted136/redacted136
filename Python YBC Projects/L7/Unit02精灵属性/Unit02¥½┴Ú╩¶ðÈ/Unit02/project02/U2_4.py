from U2_game import show_attr


class Dog():
    name = 'WangDa'   # 名字
    type = 0   # 角色属性
    max_hp = 2000   # 最大血量
    hp = max_hp     # 当前血量
    power = 999     # 攻击力
    defense = 999    # 防御力
    speed = 999       # 速度


dog_1 = Dog() # 生成实例：dog_1
dog_2 = Dog() # 生成实例：dog_2
dog_1.power = 999999  # 设置实例的攻击力为999999
print(dog_1.power, dog_2.power)
show_attr(dog_1,dog_2)  # 显示实例及其属性



