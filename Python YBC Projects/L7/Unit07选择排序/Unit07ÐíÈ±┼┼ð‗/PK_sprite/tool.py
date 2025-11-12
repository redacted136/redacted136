import os
import sys
import pygame
from pygame.locals import *

pygame.init()


ROOT_DIR = os.path.split(os.path.abspath(__file__))[0]


# 加载背景图片
BG = pygame.image.load(os.path.join(ROOT_DIR, "images/bg1.jpg"))

# 游戏画面尺寸
# SIZE = WIDTH, HEIGHT = 1024, 768
SIZE = WIDTH, HEIGHT = int(1024 * 0.8), int(768 * 0.8)

# 常用字体
FONT_YT_50 = pygame.font.Font(os.path.join(ROOT_DIR, 'font/yuanti.TTF'), int(50*0.8))
FONT_YT_30 = pygame.font.Font(os.path.join(ROOT_DIR, 'font/yuanti.TTF'), int(20*0.8))
FONT_FZ_60 = pygame.font.Font(os.path.join(ROOT_DIR, 'font/fzytj.ttf'), int(60*0.8))
FONT_FZ_30 = pygame.font.Font(os.path.join(ROOT_DIR, 'font/fzytj.ttf'), int(30*0.8))

# 颜色
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)


def text_object(text, font, color=BLACK):
    """在游戏界面显示文字"""
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


class Button(object):
    """在游戏界面显示开始结束和技能按钮"""
    def __init__(self, screen, text, color, x=None, y=None, font=FONT_YT_30):
        self.screen = screen
        self.font = font
        self.surface = self.font.render(text, True, color)
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.x = x
        self.y = y

    def display(self):
        """展示按钮到游戏界面"""
        self.screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        """判断按钮是否被点击"""
        x_match = (position[0] > self.x) and (position[0] < (self.x + self.WIDTH))
        y_match = (position[1] > self.y) and (position[1] < (self.y + self.HEIGHT))

        if x_match and y_match:
            return True
        else:
            return False


def reset(sprite1, sprite2):
    """重置游戏背景"""
    sprite1.screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))  # sprite1和sprite2的screen是一样的

    if sprite1.is_control:
        sprite1.show_dizzy_profile()
    else:
        sprite1.show_normal_profile()

    if sprite2.is_control:
        sprite2.show_dizzy_profile()
    else:
        sprite2.show_normal_profile()
    return None


def mod_1(x):
    """修改尺寸"""
    return int(x * 0.8)


def mods_1(x, y):
    """修改尺寸"""
    return int(x * 0.8), int(y * 0.8)


def mod_2(x):
    """修改尺寸"""
    return int(x * 1.2)


def mods_2(x, y):
    """修改尺寸"""
    return int(x * 1.2), int(y * 1.2)