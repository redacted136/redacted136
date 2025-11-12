from U1_game import show_attr


class Dog():
    name = 'WangDa'  # 名字
    type = 0  # 角色属性
    max_hp = 200  # 最大血量
    hp = max_hp  # 当前血量
    power = 100  # 攻击力
    defense = 50  # 防御力
    speed = 5  # 速度


dog_1 = Dog()
show_attr(dog_1)  # 显示实例dog_1及其属性


