import os
import sys
import pygame
from random import randint
from pygame.locals import *
main_dir = os.path.split(os.path.abspath(__file__))[0]
package_dir = os.path.join(main_dir, "../..")
sys.path.insert(0, package_dir)
from PK_sprite import *


pygame.init()


def start_game(dog1):
    """冒泡选择技能战斗
    对手为随机召唤兽
    对手随机释放技能
    """
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("猿力召唤师")
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    left_sprite = Sprite(screen, dog1, check_attr=True)
    dog2 = Egg()
    dog2.type = randint(0, 2)
    dog2.name = '汪汪'
    dog2.power = 1000
    right_sprite = Sprite(screen, dog2, left=False)

    left_sprite.enemy = right_sprite
    right_sprite.enemy = left_sprite

    func_list = left_sprite.egg.decision()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # 重置游戏背景
        reset(left_sprite, right_sprite)

        button_left, button_top = mods_1(450, 650)

        if type(func_list) is list and len(func_list) >= 3:   # 如果传入全部的函数那么只取评分最高的前三个技能
            func_list = func_list[:3]
        elif type(func_list) is str:  # 如果只传如第一个函数那么只展示评分最高的技能
            temp = []
            temp.append(func_list)
            func_list = temp
        
        for func_name in func_list:
            play_button = Button(screen, func_name, RED, button_left, button_top, FONT_YT_30)
            
            if play_button.check_click(pygame.mouse.get_pos()):
                play_button = Button(screen, func_name, RED, button_left, button_top, FONT_YT_30)

                if pygame.mouse.get_pressed()[0]:
                    func_list = left_sprite.egg.decision()
                    # 左边攻击
                    func = getattr(left_sprite, func_name)
                    func()

                    # 与下一回合的间隔
                    reset(left_sprite, right_sprite)
                    pygame.display.update()
                    pygame.time.wait(500)
   
                    # 右边反击
                    right_sprite.random_func()
            else:
                play_button = Button(screen, func_name, WHITE, button_left, button_top, FONT_YT_30)
            play_button.display()
            button_top += 30

        pygame.display.update()
    return None

