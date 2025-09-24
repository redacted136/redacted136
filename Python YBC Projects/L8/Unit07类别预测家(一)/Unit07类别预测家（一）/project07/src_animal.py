import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *
import pandas as pd
import numpy


data_ori = pd.read_csv('./animal.csv')
data_ori[u'标签'] = data_ori[u'标签'].map({'猫': 0, '狮子': 1})

train_data = numpy.array(data_ori[[u'鬃毛', u'体重']])

train_target = numpy.array(data_ori[[u'标签']]).ravel()

pygame.init()
size = width, height = 600, 900
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("类别预测仪")


def main(ml):
    global width, height, train_data, train_target

    image_startmenu = pygame.image.load('images_0/background/开始界面.png')  # 开始界面背景图
    image_startmenu_rect = image_startmenu.get_rect()
    image_startmenu_rect.center = (width / 2, height / 2)

    image_button = pygame.image.load('images_0/background/开始按钮.png')
    image_button_rect = image_button.get_rect()
    image_button_rect.center = (width / 2, height / 2 + 250)

    image_hair = pygame.image.load('images_0/background/鬃毛长度.png')
    image_hair_rect = image_hair.get_rect()
    image_hair_rect.center = (width / 2, height / 2 )

    image_weight = pygame.image.load('images_0/background/体重大小.png')
    image_weight_rect = image_weight.get_rect()
    image_weight_rect.center = (width / 2, height / 2 )

    image_predicting = pygame.image.load('images_0/background/正在预测.png')
    image_predicting_rect = image_predicting.get_rect()
    image_predicting_rect.center = (width / 2, height / 2 )

    image_icon = pygame.image.load('images_0/background/正在预测省略号.png')

    image_cat = pygame.image.load('images_0/background/猫.png')
    image_cat_rect = image_cat.get_rect()
    image_cat_rect.center = (width / 2, height / 2 )

    image_lion = pygame.image.load('images_0/background/狮子.png')
    image_lion_rect = image_lion.get_rect()
    image_lion_rect.center = (width / 2, height / 2 )

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

            if Gamestate == 1:  # 鬃毛长度
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
                            if len(text) < 3:
                                text += event.unicode

                screen.fill(bg)
                screen.blit(image_hair, image_hair_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 2:  # 体重大小
                colour = colourActive if active else colourInactive
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputBox.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    colour = colourActive if active else colourInactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            data.append(int(text))
                            Gamestate = 4
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            if len(text) < 4:
                                text += event.unicode

                screen.fill(bg)
                screen.blit(image_weight, image_weight_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 4:  # 预测状态显示

                screen.fill(bg)
                screen.blit(image_predicting, image_predicting_rect)

                for i in range(5):
                    screen.blit(image_icon, (width // 2 + 100 + 50 * i, height // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(500)

                Gamestate = 5
                your_data = numpy.array(data).reshape(1,-1)
                pygame.display.flip()

            if Gamestate == 5:  # 预测结果
                prediction = ml.model_use(train_data, train_target, your_data)
                category = int(prediction[0])
                if category == 0:
                    screen.fill(bg)
                    screen.blit(image_cat, image_cat_rect)
                    pygame.display.flip()

                elif category == 1:
                    screen.fill(bg)
                    screen.blit(image_lion, image_lion_rect)
                    pygame.display.flip()


        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)
