from U1_game import show_attr

class Dog():
    name = 'WangDa'  # 名字
    type = 0  # 角色属性
    max_hp = 200  # 最大血量
    hp = max_hp  # 当前血量
    power = 100  # 攻击力
    defense = 50  # 防御力
    speed = 5  # 速度

# 生成实例：dog_1


dog_1 = Dog()


# 生成实例：dog_2
dog_2 = Dog()
show_attr(dog_1, dog_2)  # 显示实例及其属性

