import pandas as pd
import csv
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pygame
import pygame.gfxdraw
import sys
from pygame.locals import *
import numpy
import random


def main(solution):
    data_ori = pd.read_csv('heros.csv')
    features_remain = [u'最大生命', u'初始生命', u'最大法力', u'初始法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝', u'最大攻速', u'攻击范围']
    #features_remain = [u'生命值', u'法力值', u'攻击力', u'防御力', u'敏捷']
    data = data_ori[features_remain]
    #data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%'))/100)
    #data[u'攻击范围'] = data[u'攻击范围'].map({'远程':1,'近战':0})
    data.replace('28.00%', 0.28, inplace=True)
    data.replace('14.00%', 0.14, inplace=True)
    data.replace('0.00%', 0.00, inplace=True)
    data.replace('42.00%', 0.42, inplace=True)
    data.replace('7.00%', 0.07, inplace=True)
    data.replace('56.00%', 0.56, inplace=True)
    data.replace('远程', 1, inplace=True)
    data.replace('近战', 0, inplace=True)

    ss = StandardScaler()
    data = ss.fit_transform(data)

    image_list = []
    for i in range(60):
        image_list.append(pygame.image.load('images/hero/' + str(i+1) + '.png'))
    ori_image = []
    for i in range(60):
        ori_image.append(pygame.image.load('images/hero/' + str(i+1) + '.png'))


    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("英雄分路AI推荐系统")

    Gamestate = 0

    image_startmenu = pygame.image.load('images/开始背景.png')  # 开始界面背景图
    image_startmenu_rect = image_startmenu.get_rect()
    image_startmenu_rect.center = (width / 2, height / 2)

    image_predicting = pygame.image.load('images/预测背景.png')
    image_predicting_rect = image_predicting.get_rect()
    image_predicting_rect.center = (width / 2, height / 2)

    image_result = pygame.image.load('images/预测结果.png')
    image_result_rect = image_result.get_rect()
    image_result_rect.center = (width / 2, height / 2)

    image_res = pygame.image.load('images/分路结果.png')
    image_res_rect = image_res.get_rect()
    image_res_rect.center = (width / 2, height / 2)

    image_button = pygame.image.load('images/开始按钮.png')
    image_button_rect = image_button.get_rect()
    image_button_rect.center = (width / 2 + 20, height / 2 + 237)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if Gamestate == 0:  # 起始界面
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and image_button_rect.collidepoint(event.pos):
                        Gamestate = 1
                screen.fill((0,0,0))
                screen.blit(image_startmenu, image_startmenu_rect)

                for i in range(10):
                    screen.blit(image_list[i], (260+70*i, 70))
                for i in range(10,20):
                    screen.blit(image_list[i], (260+70*(i-10), 140))
                for i in range(20,30):
                    screen.blit(image_list[i], (260+70*(i-20), 210))
                for i in range(30,40):
                    screen.blit(image_list[i], (260+70*(i-30), 280))
                for i in range(40,50):
                    screen.blit(image_list[i], (260+70*(i-40), 350))
                for i in range(50,60):
                    screen.blit(image_list[i], (260+70*(i-50), 420))

                screen.blit(image_button, image_button_rect)

            if Gamestate == 1:  # 预测状态显示

                screen.fill((0,0,0))
                screen.blit(image_predicting, image_predicting_rect)

                fre = 200
                for j in range(5):
                    fre = int(fre - ((j + 1) * 30))
                    for k in range(2+j*15):
                        random.shuffle(image_list)
                        for i in range(10):
                            screen.blit(image_list[i], (260+70*i, 70))
                        for i in range(10,20):
                            screen.blit(image_list[i], (260+70*(i-10), 140))
                        for i in range(20,30):
                            screen.blit(image_list[i], (260+70*(i-20), 210))
                        for i in range(30,40):
                            screen.blit(image_list[i], (260+70*(i-30), 280))
                        for i in range(40,50):
                            screen.blit(image_list[i], (260+70*(i-40), 350))
                        for i in range(50,60):
                            screen.blit(image_list[i], (260+70*(i-50), 420))
                        pygame.time.wait(fre)
                        pygame.display.flip()


                Gamestate = 2
                pygame.display.flip()

            if Gamestate == 2:  # 预测结果

                screen.fill((255,255,255))
                screen.blit(image_res, image_res_rect)  # 预测结果字样

                prediction = solution.kmeans_clustering(data)

                group0 = []
                group1 = []
                group2 = []
                group3 = []
                group4 = []

                for i in range(len(prediction)):
                    if prediction[i] == 0:
                        group0.append(ori_image[i])
                    elif prediction[i] == 1:
                        group1.append(ori_image[i])
                    elif prediction[i] == 2:
                        group2.append(ori_image[i])
                    elif prediction[i] == 3:
                        group3.append(ori_image[i])
                    elif prediction[i] == 4:
                        group4.append(ori_image[i])

                '''
                pygame.draw.rect(screen, (106,90,205), [30, 100, 1140, 110], 5)
                pygame.draw.rect(screen, (100, 149, 237), [30, 220, 1140, 110], 5)
                pygame.draw.rect(screen, (0, 205, 102), [30, 340, 1140, 110], 5)
                pygame.draw.rect(screen, (255, 236, 139), [30, 460, 1140, 110], 5)
                pygame.draw.rect(screen, (250, 128, 114), [30, 580, 1140, 110], 5)
                '''

                for i in range(len(group0)):
                    screen.blit(group0[i], (50 + 70 * i, 130))

                for i in range(len(group1)):
                    screen.blit(group1[i], (50 + 70 * i, 250))

                for i in range(len(group2)):
                    screen.blit(group2[i], (50 + 70 * i, 370))

                for i in range(len(group3)):
                    screen.blit(group3[i], (50 + 70 * i, 490))

                for i in range(len(group4)):
                    screen.blit(group4[i], (50 + 70 * i, 610))

                pygame.display.flip()

        pygame.display.flip()













