"""
show_attr(dog_1): 展示传入召唤兽的属性(不包括方法)
show_attr(dog_1, dog2): 展示传入两个召唤兽的属性(不包括方法) 同一界面展示
"""
import os
import sys
import pygame
from pygame.locals import *
main_dir = os.path.split(os.path.abspath(__file__))[0]
package_dir = os.path.join(main_dir, "../..")
sys.path.insert(0, package_dir)
from PK_sprite import *

pygame.init()


def show_attr(dog1, dog2=None):
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("猿力召唤师")
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    
    # 初始化召唤兽
    left_hero = Sprite(screen, dog1)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 只展示单个召唤兽
        if not dog2:
            left_hero.show_attr_one()
        
        # 两个召唤兽一起展示
        else:
            right_hero = Sprite(screen, dog2, False)
            left_hero.show_attr_two()
            right_hero.show_attr_two()
        pygame.display.update()
    return None



