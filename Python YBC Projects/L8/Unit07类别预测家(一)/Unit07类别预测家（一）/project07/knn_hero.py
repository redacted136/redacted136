import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *
import pandas as pd
import numpy
from sklearn.preprocessing import MinMaxScaler

data_ori = pd.read_csv('./knn_5features.csv')
dic = {} #target<-->英雄名字

hero_list = data_ori[u'英雄'].tolist()
for i in range(len(hero_list)):
    dic[i] = hero_list[i]

train_data = numpy.array(data_ori[[u'生命值', u'法力值', u'攻击力', u'防御力', u'敏捷']])

train_target = []
for i in range(len(hero_list)):
    train_target.append(i)
train_target = numpy.array(train_target)

sca = MinMaxScaler()
train_data = sca.fit_transform(train_data)

pygame.init()
size = width, height = 600, 900
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AI英雄预测仪")

def main(ml):
    global width, height, sca, train_data, train_target, hero_list, data_ori

    text_font1 = pygame.font.Font('images_1/font/a.TTF', 25)
    image_startmenu = pygame.image.load('images_1/开始界面.png')  # 开始界面背景图
    image_startmenu_rect = image_startmenu.get_rect()
    image_startmenu_rect.center = (width / 2, height / 2)

    button_icon = pygame.image.load('images_1/开始按钮.png')
    button_icon_rect = button_icon.get_rect()
    button_icon_rect.center = (width / 2, height / 2 + 280)

    image_hp = pygame.image.load('images_1/生命值.png')
    image_hp_rect = image_hp.get_rect()
    image_hp_rect.center = (width / 2, height / 2)

    image_magic = pygame.image.load('images_1/法力值.png')
    image_magic_rect = image_magic.get_rect()
    image_magic_rect.center = (width / 2, height / 2)

    image_defense = pygame.image.load('images_1/防御力.png')
    image_defense_rect = image_defense.get_rect()
    image_defense_rect.center = (width / 2, height / 2)

    image_attack = pygame.image.load('images_1/攻击力.png')
    image_attack_rect = image_attack.get_rect()
    image_attack_rect.center = (width / 2, height / 2)

    image_agile = pygame.image.load('images_1/敏捷值.png')
    image_agile_rect = image_agile.get_rect()
    image_agile_rect.center = (width / 2, height / 2)

    image_predicting = pygame.image.load('images_1/正在预测.png')
    image_predicting_rect = image_predicting.get_rect()
    image_predicting_rect.center = (width / 2, height / 2)

    image_result = pygame.image.load('images_1/结果.png')
    image_result_rect = image_result.get_rect()
    image_result_rect.center = (width / 2, height / 2)

    button_dot = pygame.image.load('images_1/正在预测省略号.png')


    image_list = []
    for i in range(len(hero_list)):
        image_list.append(pygame.image.load('images_1/hero/' + str(i) + '.jpeg'))

    font = pygame.font.Font(None, 72)
    inputBox = pygame.Rect(width / 2-100, height / 2, 100, 50)
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
                    if event.button == 1 and button_icon_rect.collidepoint(event.pos):
                        Gamestate = 1
                screen.fill((255,255,255))
                screen.blit(image_startmenu, image_startmenu_rect)
                screen.blit(button_icon, button_icon_rect)

            if Gamestate == 1:  # 生命值
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if inputBox.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    colour = colourActive if active else colourInactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            data.append(int(text.replace(' ','')))
                            Gamestate = 2
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                            if text[0] == '0':
                                text = '0'
                            if int(text) > 1000:
                                if text[:4] == '1000':
                                    text = text[:4]
                                else:
                                    text = text[:3]
                screen.fill(bg)
                screen.blit(image_hp, image_hp_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 2:  # 魔法值
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
                            Gamestate = 3
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:

                            text += event.unicode
                            if text[0] == '0':
                                text = '0'
                            if int(text) > 1000:
                                if text[:4] == '1000':
                                    text = text[:4]
                                else:
                                    text = text[:3]

                screen.fill(bg)
                screen.blit(image_magic, image_magic_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()
                
            if Gamestate == 3:  # 物理攻击
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
                            text += event.unicode
                            if text[0] == '0':
                                text = '0'
                            if int(text) > 1000:
                                if text[:4] == '1000':
                                    text = text[:4]
                                else:
                                    text = text[:3]

                screen.fill(bg)
                screen.blit(image_attack, image_attack_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()
                
            if Gamestate == 4:  # 防御力
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
                            Gamestate = 5
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                            if text[0] == '0':
                                text = '0'
                            if int(text) > 1000:
                                if text[:4] == '1000':
                                    text = text[:4]
                                else:
                                    text = text[:3]
                screen.fill(bg)
                screen.blit(image_defense, image_defense_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 5:  # 敏捷性
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

                            #放在下一个状态会出错，因为会造成循环scale
                            data_cus = numpy.array(data).reshape(1, -1)
                            data_cus = sca.transform(data_cus)

                            Gamestate = 6
                            text = ''
                            active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:

                            text += event.unicode
                            if text[0] == '0':
                                text = '0'
                            if int(text) > 1000:
                                if text[:4] == '1000':
                                    text = text[:4]
                                else:
                                    text = text[:3]
                screen.fill(bg)
                screen.blit(image_agile, image_agile_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 6:  # 预测状态显示
                
                screen.fill(bg)
                screen.blit(image_predicting, image_predicting_rect)

                for i in range(5):
                    screen.blit(button_dot, (width // 2 + 100 + 50 * i, height // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(500)

                Gamestate = 7
                pygame.display.flip()

            if Gamestate == 7:  # 预测结果

                prediction = ml.model_use(train_data, train_target, data_cus)

                screen.fill(bg)

                screen.blit(image_result, image_result_rect)

                screen.blit(image_list[prediction[0]], (0, height / 2 - 280))#预测英雄图片

                screen.blit(text_font1.render('自定义值', True, (0, 0, 0)), (width / 2 + 40, height / 2 + 152))

                screen.blit(text_font1.render(dic[prediction[0]], True, (0, 0, 0)), (width / 2 + 345, height / 2 + 152)) #预测英雄名字

                #自定义属性值
                for i in range(len(data)):
                    value = text_font1.render(str(data[i]), True, (0, 0, 0))
                    screen.blit(value, (168, height / 2 + 200 + 51 * i))

                #预测英雄属性值
                value_list = numpy.array(data_ori[[u'生命值', u'法力值', u'攻击力', u'防御力', u'敏捷']]).tolist()
                for i in range(5):
                    real = text_font1.render(str(value_list[prediction[0]][i]), True, (0, 0, 0))
                    screen.blit(real, (width / 2 + 360, height / 2 + 200 + 51 * i))

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

