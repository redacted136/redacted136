import os
import sys
import pygame
from pygame.locals import *
from .tool import *

pygame.init()


def restart(screen):
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    mes_button = Button(screen, 'YOU WIN', WHITE, mod_1(350), mod_1(320), FONT_FZ_60)
    re_button = Button(screen, 'EXIT', BLACK, mod_1(420), mod_1(520), FONT_FZ_60)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # 监听鼠标点击事件
        if pygame.mouse.get_pressed()[0]:
            if re_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
        
        # 设置按钮鼠标悬停效果
        if re_button.check_click(pygame.mouse.get_pos()):
            color = BLACK
        else:
            color = WHITE
        re_button = Button(screen, 'EXIT', color, mod_1(420), mod_1(520), FONT_FZ_60)

        mes_button.display()
        re_button.display()
        pygame.display.update()
    return None


def restart_win(screen):
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    mes_button = Button(screen, 'YOU WIN', WHITE, mod_1(350), mod_1(320), FONT_FZ_60)
    re_button = Button(screen, 'EXIT', BLACK, mod_1(420), mod_1(520), FONT_FZ_60)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            if re_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

        # 设置按钮鼠标悬停效果
        if re_button.check_click(pygame.mouse.get_pos()):
            color = BLACK
        else:
            color = WHITE
        re_button = Button(screen, 'EXIT', color,  mod_1(420), mod_1(520), FONT_FZ_60)

        mes_button.display()
        re_button.display()
        pygame.display.update()
    return None


def restart_lose(screen):
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))
    mes_button = Button(screen, 'YOU LOSE', WHITE, mod_1(350), mod_1(320), FONT_FZ_60)
    re_button = Button(screen, 'EXIT', BLACK, mod_1(420), mod_1(520), FONT_FZ_60)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_pressed()[0]:
            if re_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
        
        # 设置按钮鼠标悬停效果
        if re_button.check_click(pygame.mouse.get_pos()):
            color = BLACK
        else:
            color = WHITE
        re_button = Button(screen, 'EXIT', color, mod_1(420), mod_1(520), FONT_FZ_60)

        mes_button.display()
        re_button.display()
        pygame.display.update()
    return None


def attr_bug(screen):
    screen.blit(pygame.transform.scale(BG, SIZE), (0, 0))

    mes_button = Button(screen, '你的总属性超标，请重设召唤兽!', WHITE, mod_1(100), mod_1(270 - 50), FONT_FZ_60)
    re_button = Button(screen, 'EXIT', BLACK, mod_1(460 + 10), mod_1(470 - 50), FONT_FZ_60)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed()[0]:
            if re_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

        # 设置按钮鼠标悬停效果
        if re_button.check_click(pygame.mouse.get_pos()):
            re_button = Button(screen, 'EXIT', BLACK, mod_1(460+10), mod_1(470-50), FONT_FZ_60)
        else:
            re_button = Button(screen, 'EXIT', WHITE, mod_1(460+10), mod_1(470-50), FONT_FZ_60)

        mes_button.display()
        re_button.display()
        pygame.display.update()
    return None
