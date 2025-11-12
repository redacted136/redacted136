import random
import pygame
from pygame.locals import *
from .tool import *
from .over import *

SIZE = WIDTH, HEIGHT = 1024, 768
WAIT_TIME = 1000


class Egg:
    """用于初始化Sprite对象的类
    伤害治疗的值都是整数
    """
    def __init__(self, name='怪兽', type=3, hp=2000, power=500, defense=450, speed=50):
        self.name = name         # 名字
        self.hp = hp             # 生命值
        self.max_hp = hp         # 最大生命值
        self.power = power       # 攻击力
        self.defense = defense   # 防御力
        self.speed = speed       # 速度 通过比较决定是否先手攻击
        self.type = type         # 属性 0:fire  1:water  2:grass  3:monster

    @staticmethod
    def decision():
        """随机选择一个技能释放"""
        func_list = ['attack', 'attack_buff', 'control', 'defense_buff', 'heal', 'leech']
        return random.choice(func_list)
        
    def attack(self):
        print(f'{self.name}使用了攻击技能！')
        return self.power

    def control(self):
        if random.randint(0, 9) >= 5:
            print(f'{self.name}使用了眩晕技能！命中')
            return True
        else:
            print(f'{self.name}使用了眩晕技能！未命中')
            return False

    def leech(self):
        print(f'{self.name}使用了吸血攻击技能！')
        damage = int(self.power * 0.6)
        self.hp += int(damage * 0.5)
        return damage

    def heal(self):
        print(f'{self.name}使用了治疗技能！')
        self.hp += int(self.max_hp * 0.6)

    def attack_buff(self):
        print(self.name, "使用了攻击力增强技能！")
        self.power = int(self.power * 1.05)

    def defense_buff(self):
        print(self.name, "使用了防御力增强技能！")
        self.defense = int(self.defense * 1.05)


class Sprite:
    """召唤兽类"""
    def __init__(self, screen, egg=Egg(), left=True, check_attr=False):
        # TODO 判断传入的egg是否为一个类 不是就引发异常
        self.screen = screen      # 游戏界面句柄
        self.egg = egg            # 绑定学生自定义的召唤兽
        self.left = left          # 是否为左边召唤兽
        self.attr_list = []       # 固定属性列表 实例化的时候添加
        self.image_dict = {}      # 图片字典
        self.enemy = None         # 对手
        self.is_control = False   # 是否被眩晕
        self.control_num = 0      # 被眩晕的回合数
        
        # 设定默认值
        self.name = 'WangDa'      # 名字
        self.max_hp = 200         # 血槽
        self.hp = 200             # 血量
        self.power = 100          # 攻击力
        self.defense = 50         # 防御力
        self.speed = 5            # 速度 通过比较决定是否先手攻击
        self.type = 0             # 属性 0:fire  1:water  2:grass  3:monster
        
        # 根据学生自定义类属性来设置召唤兽的属性
        if hasattr(egg, 'name'):
            self.name = egg.name
        if hasattr(egg, 'max_hp'):
            self.max_hp = egg.max_hp
        else:
            self.max_hp = egg.hp  # 如果没有提供最大血量属性就用初始化时的血量作为最大血量
        if hasattr(egg, 'hp'):
            self.hp = egg.hp
        if hasattr(egg, 'power'):
            self.power = egg.power
        if hasattr(egg, 'defense'):
            self.defense = egg.defense
        if hasattr(egg, 'speed'):
            self.speed = egg.speed
        if hasattr(egg, 'is_control'):
            self.is_control = egg.is_control
        if hasattr(egg, 'type'):
            # TODO 要不要在这里加是否为0,1,2,3的判断?
            self.type = egg.type
        
        # 判断总属性是否合法
        if check_attr:
            self.__is_legal()
        
        # 调用函数设置召唤兽外化图片
        self.__get_image_dict()
        return None

    def __is_legal(self):
        """判断召唤兽的属性是否符合要求
        属性和小于等于3000
        """
        if self.hp + self.power + self.defense + self.speed > 3000:
            return attr_bug(self.screen)

    def __get_image_dict(self):
        """根据类型获取对应的图片
        """
        self.image_dict = {
            'hammer': 'hammer.png',
            'heal_effect': 'heal_effect.png',
            'defense_effect': 'defense_effect.png',
            'power_effect': 'power_effect.png',
            'dizzy_effect': 'dizzy_effect.png',
        }
        if self.type == 1:
            self.image_dict['normal'] = 'water_normal.png'
            self.image_dict['cry'] = 'water_cry.png'
            self.image_dict['dizzy'] = 'water_dizzy.png'
            self.image_dict['attack'] = 'water_attack.png'
        elif self.type == 2:
            self.image_dict['normal'] = 'grass_normal.png'
            self.image_dict['cry'] = 'grass_cry.png'
            self.image_dict['dizzy'] = 'grass_dizzy.png'
            self.image_dict['attack'] = 'grass_attack.png'
        elif self.type == 3:
            self.image_dict['normal'] = 'monster_normal.png'
            self.image_dict['cry'] = 'monster_cry.png'
            self.image_dict['dizzy'] = 'monster_dizzy.png'
            self.image_dict['attack'] = 'monster_attack.png'
        else:
            self.image_dict['normal'] = 'fire_normal.png'
            self.image_dict['cry'] = 'fire_cry.png'
            self.image_dict['dizzy'] = 'fire_dizzy.png'
            self.image_dict['attack'] = 'fire_attack.png'
        return None
    
    def __show_image(self, image):
        """外化展示当前召唤兽的样子
        """
        # 加载召唤兽图片
        normal = pygame.image.load(os.path.join(ROOT_DIR, f"images/{image}"))
        rect = normal.get_rect()
        
        # 获取召唤兽大小和坐标
        if self.type == 0:     # 火龙
            size = (mods_1(280+20, 250+20))
            topleft = (mods_1(80-20, HEIGHT-450-30)) if self.left else (mods_1(WIDTH-350+20, HEIGHT-450-30))
        elif self.type == 2:   # 木龙
            size = (mod_1(280+20), mod_1(250+20))
            topleft = mods_1(80, HEIGHT-450-50) if self.left else mods_1((WIDTH-350), (HEIGHT-450-50))
        else:                  # 水龙和怪兽
            size = (mod_1(280), mod_1(200))
            topleft = mods_1(80, (HEIGHT-450)) if self.left else mods_1((WIDTH-350), (HEIGHT-450))
        rect.topleft = topleft
        
        # 调整图片方向并图片坐标
        if self.left:
            normal = pygame.transform.flip(normal, True, False)
        
        # 贴图
        self.screen.blit(pygame.transform.scale(normal, size), rect)
        return normal, rect
    
    def __show_image_two(self):
        """外化展示当前召唤兽的样子
        同一游戏画面展示两个召唤兽(方向一致)
        """
        # 加载召唤兽图片
        normal = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['normal']}"))
        rect = normal.get_rect()
    
        # 获取图片坐标
        if self.type == 0 or self.type == 2:
            rect.topleft = mods_1(100, HEIGHT - 450) if self.left else mods_1(WIDTH - 370, HEIGHT - 450)
            size = mods_1(280+20, 250+20)
        else:
            rect.topleft = mods_1(100, HEIGHT - 450 + 50) if self.left else mods_1(WIDTH - 370, HEIGHT - 450 + 50)
            size = mods_1(280, 200)

        # 贴图
        self.screen.blit(pygame.transform.scale(normal, size), rect)
        return None

    def __show_blood(self):
        """展示姓名和血条"""
        # 显示姓名
        name_text, name_rect = text_object("name: " + self.name, FONT_YT_30, WHITE)
        name_rect.topleft = mods_1(120-70, 650) if self.left else mods_1(750, 650)
        self.screen.blit(name_text, name_rect)
    
        # 显示血量
        blood_text, blood_rect = text_object("HP: " + str(self.hp), FONT_YT_30, WHITE)
        blood_rect.topleft = (name_rect.left, name_rect.top+mod_1(40))
        self.screen.blit(blood_text, blood_rect)
    
        # 显示血条 血条的长度和血量数值相关
        blood_bar_left = blood_rect.left
        blood_bar_top = (blood_rect.top + mod_1(40))
        pygame.draw.rect(self.screen, WHITE, ((blood_bar_left, blood_bar_top), (self.max_hp / 10, 10)), width=3)
        blood_bar_len = (self.hp / self.max_hp) * self.max_hp / 10
        pygame.draw.rect(self.screen, RED, ((blood_bar_left, blood_bar_top), (blood_bar_len, 10)))
        return None

    def __is_control_status(self):
        """处理眩晕状态"""
        # 如果还剩余多个控制回合则只是次数减一
        if self.control_num > 1:
            text = FONT_YT_30.render(self.name + f'被眩晕，当前回合无法攻击，剩余{self.control_num - 1}回合', False, WHITE)
            reset(self, self.enemy)
            self.screen.blit(text, mods_1(300, 660))
            pygame.display.update()
            pygame.time.wait(3000)
            self.control_num -= 1
            return True
        
        # 只剩余一个回合时 需要在回合结束后把眩晕状态改为正常状态
        elif self.control_num == 1:
            text = FONT_YT_30.render(self.name + f'被眩晕，当前回合无法攻击，剩余{self.control_num - 1}回合', False, WHITE)
            reset(self, self.enemy)
            self.screen.blit(text, mods_1(300, 660))
            pygame.display.update()
            pygame.time.wait(3000)
            self.control_num -= 1
            self.is_control = False
            pygame.display.update()
            return True
        else:
            return False

    def show_attr_one(self):
        """外化展示当前召唤兽的属性"""
        attr_top = mod_1(100)  # 属性的纵坐标
        attr_list = ['name', 'type', 'max_hp', 'hp', 'power', 'defense', 'speed']
        
        # 展示召唤兽
        self.__show_image(self.image_dict['normal'])
        
        # 展示属性的背景框
        text_image = pygame.image.load(os.path.join(ROOT_DIR, 'images/text.png'))
        text_rect = text_image.get_rect()
        text_rect.topleft = mods_1(500, 125)
        self.screen.blit(pygame.transform.scale(text_image, mods_1(250, 380)), text_rect)
        
        # 展示固有属性
        for attr in attr_list:
            attr_top += mod_1(50)
            attr, attr_rect = text_object(f"{attr} : {getattr(self.egg, attr, '')}", FONT_YT_30)
            attr_rect.topleft = (mod_1(550), attr_top)
            self.screen.blit(attr, attr_rect)
        return None

    def show_attr_two(self):
        """外化展示当前召唤兽的属性
        同一游戏画面展示两个召唤兽
        """
        # attr_top = mod_1(50)  # 属性的纵坐标
        attr_top = 50  # 属性的纵坐标
        attr_list = ['name', 'type', 'max_hp', 'hp', 'power', 'defense', 'speed']
    
        # 展示召唤兽
        self.__show_image_two()
    
        # 展示属性的背景框
        text_image = pygame.image.load(os.path.join(ROOT_DIR, 'images/text.png'))
        text_rect = text_image.get_rect()
        if self.left:
            text_rect.topleft = mods_1(200-50, 125-70)
        else:
            text_rect.topleft = mods_1(500+190-20, 125-70)
        self.screen.blit(pygame.transform.scale(text_image, mods_1(200, 250)), text_rect)
    
        # 展示固有属性
        for attr in attr_list:
            # attr_top += mod_1(30)
            attr_top += 30
            attr, attr_rect = text_object(f"{attr} : {getattr(self.egg, attr, '')}", FONT_YT_30)
            if self.left:
                attr_rect.topleft = mods_1(170, attr_top)
            else:
                attr_rect.topleft = mods_1(710-20, attr_top)
            self.screen.blit(attr, attr_rect)
        return None

    def show_normal_profile(self):
        self.__show_image(self.image_dict['normal'])
        self.__show_blood()

    def show_cry_profile(self):
        self.__show_image(self.image_dict['cry'])
        self.__show_blood()
        return None

    def show_dizzy_profile(self):
        self.__show_image(self.image_dict['dizzy'])
        self.__show_blood()
        return None

    def get_func_list(self):
        """筛选出学生自定义的方法"""
        exclusion_list = ['name', 'type', 'max_hp', 'hp', 'power', 'defense', 'speed']
        result_list = []
        for n in dir(self.egg):
            if n[0] != '_' and n[-1] != '_':
                if n not in exclusion_list:
                    if type(type(self.egg).__dict__.get(n)) != int and type(
                            type(self.egg).__dict__.get(n)) != str:
                        result_list.append(str(n))
        return result_list

    def handle_hp(self, v):
        """处理血量
        受伤传进来负数
        治疗传进来正数
        """
        # 更新血量 取整
        self.hp += int(v)
        
        # 判断是否过最大血量
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
        # 判断是否血量为负数
        if self.hp < 0:
            self.hp = 0
        
        # 判断游戏输赢
        if self.hp == 0:
            if self.left:
                return restart_lose(self.screen)
            else:
                return restart_win(self.screen)
            
        # 更新血量到学生自定义召唤兽
        self.egg.hp = self.hp
        return None

    def attack(self):
        """攻击函数"""
        if self.__is_control_status():
            return None

        # 执行初始化类的攻击函数获取伤害值
        damage = self.egg.attack()
        
        # 外化攻击效果
        attack = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['attack']}"))
        rect = attack.get_rect()

        # 获取攻击技能的坐标的尺寸
        if self.type == 2:   # 木龙
            size = mods_1(250, 250)
            topleft = mods_1(350, 260+20) if self.left else mods_1(420, 260+20)
        else:
            size = mods_1(250, 250)
            topleft = mods_1(350, 260) if self.left else mods_1(420, 260)

        # monster的attack图和其他的尺寸不一样需要单独调整
        if self.image_dict['attack'] == 'monster_attack.png':
            size = mods_1(300, 140)
            topleft = mods_1(350, 350) if self.left else mods_1(350, 350)
            
        if self.left:
            attack = pygame.transform.flip(attack, True, False)

        rect.topleft = topleft
        self.screen.blit(pygame.transform.scale(attack, size), rect)
        pygame.display.update()
        pygame.time.wait(500)   # 这里从1000改成500 不然会有卡顿感觉
        
        # 计算伤害 如果攻击力小于等于防御力则强制造成一点伤害
        if self.left:
            v = damage - self.enemy.defense if damage - self.enemy.defense > 0 else 1
        else:
            v = self.power - self.enemy.defense if self.power - self.enemy.defense > 0 else 1
        
        # 展示攻击效果
        self.enemy.handle_hp(-v)
        reset(self, self.enemy)
        self.enemy.show_cry_profile()
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)
        reset(self, self.enemy)
        return None
    
    def heal(self):
        """治疗技能"""
        if self.__is_control_status():
            return None
        
        self.egg.heal()
        self.hp = int(self.egg.hp)   # 利用类型转换保证血量为整数

        # 判断血量是否合法
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.hp < 0:
            self.hp = 0

        # 更新精灵血量到学生自定义召唤兽
        self.egg.hp = self.hp

        # 外化治疗效果
        heal_effect = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['heal_effect']}"))
        heal_effect = pygame.transform.rotate(heal_effect, 0)
        rect = heal_effect.get_rect()
        rect.topleft = mods_1(-70, 250) if self.left else mods_1(480, 250)
        self.screen.blit(pygame.transform.scale(heal_effect, mods_1(600, 400)), rect)
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)
        reset(self, self.enemy)
        return None
    
    def leech(self):
        if self.__is_control_status():
            return None
        
        self.attack()
        self.heal()
        return None
    
    def control(self):
        """眩晕攻击
        """
        if self.__is_control_status():
            return None

        reset(self, self.enemy)

        # 不论攻击是否生效都要展示攻击效果
        hammer = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['hammer']}"))
        hammer = pygame.transform.rotate(hammer, 0)
        hammer_rect = hammer.get_rect()
        if self.left:
            hammer_rect.topleft = mods_1(390, 200)
        else:
            hammer = pygame.transform.flip(hammer, True, False)
            hammer_rect.topleft = mods_1(160, 200)
        self.screen.blit(pygame.transform.scale(hammer, mods_1(500, 300)), hammer_rect)
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)

        # 判断攻击是否生效
        if self.egg.control():
            self.enemy.control_num = 2  # 眩晕从一回合改成两回合
            self.enemy.is_control = True
            self.enemy.show_dizzy_profile()
            pygame.display.update()
        else:
            text = FONT_YT_30.render(self.name + f'眩晕技能未命中', False, WHITE)
            self.screen.blit(text, mods_1(400, 660))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.display.update()
        reset(self, self.enemy)
        return None
       
    def attack_buff(self):
        if self.__is_control_status():
            return None
        
        # 同步攻击力
        self.egg.attack_buff()
        self.power = int(self.egg.power)
        print(f'攻击力增强为{self.power}')
        
        # 展示效果
        topleft = mods_1(30, 300) if self.left else mods_1(580, 300)
        image = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['power_effect']}"))
        rect = image.get_rect()
        rect.topleft = topleft
        self.screen.blit(pygame.transform.scale(image, mods_1(400, 200)), rect)
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)
        return None
    
    def defense_buff(self):
        if self.__is_control_status():
            return None
        
        # 同步攻击力
        self.egg.defense_buff()
        self.power = int(self.egg.defense)
        print(f'防御力增强为{self.power}')
        
        # 展示效果
        topleft = mods_1(30, 300) if self.left else mods_1(580, 300)
        image = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['defense_effect']}"))
        rect = image.get_rect()
        rect.topleft = topleft
        self.screen.blit(pygame.transform.scale(image, mods_1(400, 200)), rect)
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)
        return None

    def random_func(self, all=True):
        if all:
            func_list = ['attack', 'heal', 'control', 'leech', 'attack_buff', 'defense_buff']
        else:
            func_list = ['attack', 'heal']
        func_name = random.choice(func_list)
        if func_name in func_list:
            func = getattr(self, func_name)
            is_control = func()
            return func_name, is_control

    def random_func_by_name(self, func_name):
        func_list = ['attack', 'heal', 'control', 'leech', 'attack_buff', 'defense_buff']
        if func_name in func_list:
            func = getattr(self, func_name)
            is_control = func()
            return func_name, is_control


class SpriteSon(Sprite):
    """实现show_func函数中根据攻击力喷大火和小火的效果
    只有在show_attr函数中才用这个类
    大火小火取决于attack()函数的返回值
    大于1000喷大火 否则喷小火
    """
    def attack(self):
        """攻击函数"""
        # 获取伤害值
        damage = self.egg.attack()
        
        # 加载技能图片
        attack = pygame.image.load(os.path.join(ROOT_DIR, f"images/{self.image_dict['attack']}"))
        if self.left:
            attack = pygame.transform.flip(attack, True, False)
        rect = attack.get_rect()
        
        # 由attack函数的值来决定攻击效果
        if damage < 1000:
            size = mods_1(250, 250)
            topleft = mods_1(350, 260) if self.left else mods_1(420, 250)
        
        # 大火
        else:
            size = mods_1(400, 400)
            topleft = mods_1(300-30, 160) if self.left else mods_1(420-80, 160)
        
        # monster的attack图和其他的尺寸不一样需要单独调整
        if self.image_dict['attack'] == 'monster_attack.png':
            size = mods_1(300, 140)
            topleft = mods_1(350, 350)
            
        rect.topleft = topleft
        self.screen.blit(pygame.transform.scale(attack, size), rect)
        pygame.display.update()
        pygame.time.wait(500)  # 这里从1000改成500 不然会有卡顿感觉
        
        # 计算伤害
        if self.left:
            v = damage - self.enemy.defense if damage - self.enemy.defense > 0 else 1
        else:
            v = self.power - self.enemy.defense if self.power - self.enemy.defense > 0 else 1
        
        # 展示效果
        self.enemy.handle_hp(-v)
        reset(self, self.enemy)
        self.enemy.show_cry_profile()
        pygame.display.update()
        pygame.time.wait(WAIT_TIME)
        reset(self, self.enemy)
        return None
