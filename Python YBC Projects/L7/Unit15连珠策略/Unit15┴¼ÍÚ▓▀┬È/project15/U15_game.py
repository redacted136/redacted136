# -*- coding: utf-8 -*-

import numpy as np
import sys
import random
import pygame
from pygame.locals import *
import pygame.gfxdraw

class Checkerboard:
    def __init__(self, line_points):
        self._line_points = line_points
        self._checkerboard = np.zeros((self._line_points,self._line_points))

    def get_checkerboard(self):
        return self._checkerboard

    # checkerboard = property(_get_checkerboard)

    # 判断是否可落子
    def can_drop(self, point):
        return self._checkerboard[point.Y][point.X] == 0

    def drop(self, chessman_color, point):
        """
        落子
        :param chessman:
        :param point:落子位置
        :return:若该子落下之后即可获胜，则返回获胜方，否则返回 None
        """
        print('%s on %d row %d column'% ('black' if chessman_color == 1 else 'white', point.Y,  point.X ))
        self._checkerboard[point.Y][point.X] = chessman_color

        if self._win(point):
            print('%s 获胜' % ('black' if chessman_color == 1 else 'white'))
            return chessman_color

    # 判断是否赢了
    def _win(self, point):
        cur_value = self._checkerboard[point.Y][point.X]
        for os in offset:
            if self._get_count_on_direction(point, cur_value, os[0], os[1]):
                return True

    def _get_count_on_direction(self, point, value, x_offset, y_offset):
        count = 1
        for step in range(1, 5):                #正向判断
            x = point.X + step * x_offset
            y = point.Y + step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                count += 1
            else:
                break
        for step in range(1, 5):                #反向判断
            x = point.X - step * x_offset
            y = point.Y - step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                count += 1
            else:
                break

        return count >= 5                       #相加大于等于5返回true

class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y


offset = [(1, 0), (0, 1), (1, 1), (1, -1)]

SIZE = 30  # 棋盘每个点时间的间隔
Line_Points = 15  # 棋盘每行/每列点数
Outer_Width = 20  # 棋盘外宽度
Border_Width = 4  # 边框宽度
Inside_Width = 20  # 边框跟实际的棋盘之间的间隔
Border_Length = SIZE * (Line_Points - 1) + Inside_Width * 2 + Border_Width  # 边框线的长度
Start_X = Start_Y = Outer_Width + int(Border_Width / 2) + Inside_Width  # 网格线起点（左上角）坐标
SCREEN_HEIGHT = SIZE * (Line_Points - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2  # 游戏屏幕的高
SCREEN_WIDTH = SCREEN_HEIGHT   # 游戏屏幕的宽

Stone_Radius = SIZE // 2 - 3  # 棋子半径
Stone_Radius2 = SIZE // 2 + 3
Checkerboard_Color = (0xE3, 0x92, 0x65)  # 棋盘颜色
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (200, 30, 30)
BLUE_COLOR = (30, 30, 200)
BLACK_STONE = (45,45,45)
WHITE_STONE = (219,219,219)


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


def start_game(AIPlayer):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('壮猿五子棋')
    font2 = pygame.font.SysFont('arial', 72)
    fwidth, fheight = font2.size('Black WIN')

    checkerboard = Checkerboard(Line_Points)
    #AIPlayer.color = 1 if random.randint(0, 9) < 5 else 2
    print('Player: %s , AI : %s' % (('white', 'black') if AIPlayer.color == 1 else ('black', 'white')))
    cur_runner = 1
    winner = None
    # computer = AI(Line_Points, BLACK_CHESSMAN)
    if AIPlayer.color ==1:
        cor = AIPlayer.decision(checkerboard.get_checkerboard())
        AI_point = Point(cor[1],cor[0])
        checkerboard.drop(AIPlayer.color, AI_point)
        _draw_checkerboard(screen)
        cur_runner = 2

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if winner is not None:
                        winner = None
                        cur_runner = 1
                        checkerboard = Checkerboard(Line_Points)
                        # computer = AI(Line_Points, BLACK_CHESSMAN)
            elif event.type == MOUSEBUTTONDOWN:
                if winner is None:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:
                        mouse_pos = pygame.mouse.get_pos()
                        click_point = _get_clickpoint(mouse_pos)   #得到落点坐标(x, y)
                        if click_point is not None:
                            if checkerboard.can_drop(click_point):
                                winner = checkerboard.drop(cur_runner, click_point)
                                if winner is None:
                                    cur_runner = _get_next(cur_runner)
                                    cor = AIPlayer.decision(checkerboard.get_checkerboard())
                                    AI_point = Point(cor[1],cor[0])
                                    winner = checkerboard.drop(cur_runner, AI_point)
                                    cur_runner = _get_next(cur_runner)

                        else:
                            print('超出棋盘区域')

        # 画棋盘
        _draw_checkerboard(screen)

        # 画棋盘上已有的棋子
        for i, row in enumerate(checkerboard.get_checkerboard()):
            for j, cell in enumerate(row):
                if cell == 1:
                    _draw_chessman(screen, Point(j, i), BLACK_STONE)
                elif cell == 2:
                    _draw_chessman(screen, Point(j, i), WHITE_STONE)



        #打印胜者信息
        if winner:
            print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2 - 25, (SCREEN_HEIGHT - fheight) // 2,
                       ('BLACK' if winner ==1 else 'WHITE') + ' WIN', RED_COLOR)

        #fcclock.tick(fps)
        pygame.display.flip()


def _get_next(cur_runner):
    if cur_runner == 1:
        return 2
    else:
        return 1


# 画棋盘
def _draw_checkerboard(screen):
    # 填充棋盘背景色
    screen.fill(Checkerboard_Color)
    # 画棋盘网格线外的边框
    pygame.draw.rect(screen, BLACK_COLOR, (Outer_Width, Outer_Width, Border_Length, Border_Length), Border_Width)
    # 画网格线
    for i in range(Line_Points):
        pygame.draw.line(screen, BLACK_COLOR,
                         (Start_Y, Start_Y + SIZE * i),
                         (Start_Y + SIZE * (Line_Points - 1), Start_Y + SIZE * i),
                         1)
    for j in range(Line_Points):
        pygame.draw.line(screen, BLACK_COLOR,
                         (Start_X + SIZE * j, Start_X),
                         (Start_X + SIZE * j, Start_X + SIZE * (Line_Points - 1)),
                         1)

    # 可落子处标记圆形边框
    for i in range(Line_Points):
        for j in range(Line_Points):
            pygame.gfxdraw.aacircle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, 2, BLACK_COLOR)


# 画棋子
def _draw_chessman(screen, point, stone_color):
    pygame.gfxdraw.aacircle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)
    pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)

# 根据鼠标点击位置，返回游戏区坐标
def _get_clickpoint(click_pos):
    pos_x = click_pos[0] - Start_X
    pos_y = click_pos[1] - Start_Y
    if pos_x < -Inside_Width or pos_y < -Inside_Width:
        return None
    x = pos_x // SIZE
    y = pos_y // SIZE
    if pos_x % SIZE > Stone_Radius:
        x += 1
    if pos_y % SIZE > Stone_Radius:
        y += 1
    if x >= Line_Points or y >= Line_Points:
        return None

    return Point(x, y)
