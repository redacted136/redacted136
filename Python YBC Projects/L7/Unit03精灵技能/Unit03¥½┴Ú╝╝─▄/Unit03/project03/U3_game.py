import os
import sys
import random
import pygame
from pygame.locals import *
main_dir = os.path.split(os.path.abspath(__file__))[0]
package_dir = os.path.join(main_dir, "../..")
sys.path.insert(0, package_dir)
from PK_sprite import *

"""
回合制战斗直到游戏结束
伤害=攻击力-防御力
"""
import os
import sys
import pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
package_dir = os.path.join(main_dir, "../..")
sys.path.append(package_dir)
from PK_sprite import *


pygame.init()


class Monster:
    # 固定属性如下
    name = 'monster'
    type = 3
    max_hp = 2000
    hp = max_hp
    power = 1200
    defense = 400
    speed = 999

    def attack(self):
        return self.power
    
    def heal(self):
        self.hp += self.max_hp * 0.6
        return


def show_func(dog1):
    """展示喷火技能"""
    dog2 = Monster()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("猿力召唤师")
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    left_sprite = SpriteSon(screen, dog1)
    right_sprite = SpriteSon(screen, dog2, left=False)

    left_sprite.enemy = right_sprite
    right_sprite.enemy = left_sprite

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 重置游戏背景
        reset(left_sprite, right_sprite)
        play_button = Button(screen, 'attack', WHITE, mod_1(450), mod_1(650), FONT_YT_30)

        # 攻击按钮和效果
        if play_button.check_click(pygame.mouse.get_pos()):
            # 设置按钮鼠标悬停效果
            play_button = Button(screen, 'attack', RED, mod_1(450), mod_1(650), FONT_YT_30)

            # 如果被点击则释放技能
            if pygame.mouse.get_pressed()[0]:
                # 展示攻击效果
                left_sprite.attack()

        play_button.display()
        pygame.display.update()
    return None


def start_game(dog1):
    """展示喷火技能"""
    dog2 = Monster()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("猿力召唤师")
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    left_sprite = Sprite(screen, dog1)
    right_sprite = Sprite(screen, dog2, left=False)  # TODO 后面这里替换成怪兽

    left_sprite.enemy = right_sprite
    right_sprite.enemy = left_sprite

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # 重置游戏背景
        reset(left_sprite, right_sprite)
        button_left, button_top = mods_1(450, 650)
        for func_name in left_sprite.get_func_list():
            play_button = Button(screen, func_name, RED, button_left, button_top, FONT_YT_30)
            
            # 设置按钮鼠标悬停效果
            if play_button.check_click(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    # 左边攻击
                    func = getattr(left_sprite, func_name)
                    func()

                    # 重置背景
                    reset(left_sprite, right_sprite)
                    pygame.display.update()
                    pygame.time.wait(500)
                    
                    # 右边反击
                    right_sprite.random_func(all=False)
            else:
                play_button = Button(screen, func_name, WHITE, button_left, button_top, FONT_YT_30)
            play_button.display()
            button_top += 30

        pygame.display.update()
    return None

