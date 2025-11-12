import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *
import pandas as pd
import numpy
from sklearn.preprocessing import MinMaxScaler


data_ori = pd.read_csv('hero.csv')

train_data = numpy.array(data_ori[[u'生命值', u'敏捷']])

train_target = numpy.array(data_ori[[u'类型']][u'类型'].map({'刺客':0,'非刺客':1}))   #刺客类型对应0、非刺客类型对应1。

sca = MinMaxScaler()
train_data = sca.fit_transform(train_data)

pygame.init()
size = width, height = 600, 900
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AI英雄类型预测仪")

def main(ml):
    global width, height, sca, train_data, train_target, data_ori

    image_startmenu = pygame.image.load('images/开始界面.png')  # 开始界面背景图
    image_startmenu_rect = image_startmenu.get_rect()
    image_startmenu_rect.center = (width / 2, height / 2)

    button_icon = pygame.image.load('images/开始按钮.png')
    button_icon_rect = button_icon.get_rect()
    button_icon_rect.center = (width / 2, height / 2 + 280)

    image_hp = pygame.image.load('images/生命值.png')
    image_hp_rect = image_hp.get_rect()
    image_hp_rect.center = (width / 2, height / 2)

    image_magic = pygame.image.load('images/法力值.png')
    image_magic_rect = image_magic.get_rect()
    image_magic_rect.center = (width / 2, height / 2)

    image_defense = pygame.image.load('images/防御力.png')
    image_defense_rect = image_defense.get_rect()
    image_defense_rect.center = (width / 2, height / 2)

    image_attack = pygame.image.load('images/攻击力.png')
    image_attack_rect = image_attack.get_rect()
    image_attack_rect.center = (width / 2, height / 2)

    image_agile = pygame.image.load('images/敏捷值.png')
    image_agile_rect = image_agile.get_rect()
    image_agile_rect.center = (width / 2, height / 2)

    image_predicting = pygame.image.load('images/正在预测.png')
    image_predicting_rect = image_predicting.get_rect()
    image_predicting_rect.center = (width / 2, height / 2)

    image_w = pygame.image.load('images/非刺客.png')
    image_w_rect = image_w.get_rect()
    image_w_rect.center = (width / 2, height / 2)

    image_m = pygame.image.load('images/刺客.png')
    image_m_rect = image_m.get_rect()
    image_m_rect.center = (width / 2, height / 2)

    button_dot = pygame.image.load('images/正在预测省略号.png')


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
                screen.fill((255, 255, 255))
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
                            data.append(int(text.replace(' ', '')))
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

            if Gamestate == 2:  # 敏捷性
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

                            # 放在下一个状态会出错，因为会造成循环scale
                            data_cus = numpy.array(data).reshape(1, -1)
                            data_cus = sca.transform(data_cus)

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
                screen.blit(image_agile, image_agile_rect)
                txtSurface = font.render(text, True, colour)
                width = max(200, txtSurface.get_width() + 10)
                inputBox.w = width
                screen.blit(txtSurface, (inputBox.x + 5, inputBox.y + 5))
                pygame.draw.rect(screen, colour, inputBox, 2)
                pygame.display.flip()

            if Gamestate == 3:  # 预测状态显示

                screen.fill(bg)
                screen.blit(image_predicting, image_predicting_rect)

                for i in range(5):
                    screen.blit(button_dot, (width // 2 + 100 + 50 * i, height // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(500)

                Gamestate = 4
                pygame.display.flip()

            if Gamestate == 4:  # 预测结果

                prediction = ml.model_use(train_data, train_target, data_cus)
                screen.fill(bg)

                if prediction[0] == 0: #刺客
                    screen.blit(image_m, image_m_rect)

                    Gamestate = 5
                    pygame.display.flip()

                elif prediction[0] == 1: #非刺客
                    screen.blit(image_w, image_w_rect)

                    Gamestate = 6
                    pygame.display.flip()

                pygame.display.flip()

            if Gamestate == 5: #避免未设置random_state造成的预测结果不同

                screen.fill(bg)
                screen.blit(image_m, image_m_rect)
                pygame.display.flip()

            if Gamestate == 6: #避免未设置random_state造成的预测结果不同

                screen.fill(bg)
                screen.blit(image_w, image_w_rect)
                pygame.display.flip()

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

