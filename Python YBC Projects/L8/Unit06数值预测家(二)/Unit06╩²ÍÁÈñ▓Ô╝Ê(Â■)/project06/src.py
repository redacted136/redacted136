import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *
import pandas as pd
import numpy

data_ori = pd.read_csv('./height_data.csv')

train_data = numpy.array(data_ori[[u'父亲身高']])

train_target = numpy.array(data_ori[[u'孩子身高']])


pygame.init()
size = width, height = 600, 900
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("身高预测仪")


def main(ml):
    global width, height, train_data, train_target

    text_font1 = pygame.font.Font('images/font/a.TTF', 60)
    image_startmenu = pygame.image.load('images/background/1.png')  # 开始界面背景图
    image_startmenu_rect = image_startmenu.get_rect()
    image_startmenu_rect.center = (width / 2, height / 2)

    image_background1 = pygame.image.load('images/background/父亲身高.png')
    #image_background2 = pygame.image.load('images/background/母亲身高.png')
    #image_background3 = pygame.image.load('images/background/您的性别.png')
    image_background4 = pygame.image.load('images/background/正在预测.png')
    image_background5 = pygame.image.load('images/background/预测结果.png')

    image_icon = pygame.image.load('images/background/正在预测省略号.png')
    image_button = pygame.image.load('images/background/按钮.png')
    image_button_rect = image_button.get_rect()
    image_button_rect.center = (width / 2, height / 2)

    font = pygame.font.Font(None, 72)
    inputBox = pygame.Rect(width / 2 - 100, height / 2, 100, 50)
    colourInactive = pygame.Color('lemonchiffon1')
    colourActive = pygame.Color('gold1')
    colour = colourInactive
    text = ''
    data = []

    active = False
    Gamestate = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if Gamestate == 0:  # 起始界面
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and image_button_rect.collidepoint(event.pos):
                        Gamestate = 1
                screen.fill((255, 255, 255))
                screen.blit(image_startmenu, image_startmenu_rect)
                screen.blit(image_button, image_button_rect)

            if Gamestate == 1:  # 父亲身高
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputBox.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    colour = colourActive if active else colourInactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            data.append(int(text.replace(' ', '')))
                            Gamestate = 2
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

                screen.fill(bg)
                screen.blit(image_background1, (0, 0))
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 2:  # 预测状态显示

                screen.fill(bg)
                screen.blit(image_background4, (0, 0))

                for i in range(5):
                    screen.blit(image_icon, (width // 2 + 100 + 50 * i, height // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(500)

                Gamestate = 3
                your_data = numpy.array(data).reshape(1, -1)
                pygame.display.flip()

            if Gamestate == 3:  # 预测结果
                prediction = ml.model_use(train_data, train_target, your_data)
                height = int(prediction[0][0])

                result = text_font1.render(str(height) + 'cm', True, (227, 207, 87))
                result_rect = result.get_rect()
                result_rect.center = (300, 400)

                screen.fill(bg)
                screen.blit(image_background5, (0, 0))
                screen.blit(result, result_rect)

                pygame.display.flip()

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)


