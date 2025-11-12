import sys
import pygame
from pygame.locals import *
import pygame.gfxdraw
from collections import namedtuple
import numpy as np



class Checkerboard:
    def __init__(self, line_points, arr, dim):
        self._line_points = line_points
        if dim == 1:
            self._checkerboard = [arr.tolist()]
        elif dim == 2:
            self._checkerboard = arr.tolist()

    def _get_checkerboard(self):
        return self._checkerboard

    checkerboard = property(_get_checkerboard)


    # 判断是否可落子
    def can_drop(self, point):
        return self._checkerboard[point.Y][point.X] == 0

    def drop(self, chessman, point):
        """
        落子
        :param chessman:
        :param point:落子位置
        :return:若该子落下之后即可获胜，则返回获胜方，否则返回 None
        """
        #print(f'{chessman.Name} ({point.X}, {point.Y})')
        print(chessman.Name, "：array[", point.Y, "][", point.X, "] = ", chessman.Value, sep='')
        self._checkerboard[point.Y][point.X] = chessman.Value


def init_parameters(array):
    global SCREEN_HEIGHT, SCREEN_WIDTH, SIZE, dim, arr, image_bg
    global Line_Points_x, Line_Points_y
    global Outer_Width, Border_Width, Inside_Width, Border_Length_x, Border_Length_y, Start_X, Start_Y, SCREEN_HEIGHT, SCREEN_WIDTH, Line_Points
    global Stone_Radius, Stone_Radius2, Checkerboard_Color, BLACK_COLOR, WHITE_COLOR, RED_COLOR, BLUE_COLOR, YELLOW_COLOR
    global BLACK_STONE_COLOR, WHITE_STONE_COLOR, RIGHT_INFO_POS_X
    global Chessman, Point, BLACK_CHESSMAN, WHITE_CHESSMAN

    Chessman = namedtuple('Chessman', 'Name Value Color')
    Point = namedtuple('Point', 'X Y')

    BLACK_CHESSMAN = Chessman('黑子', 1, (45, 45, 45))
    WHITE_CHESSMAN = Chessman('白子', 2, (219, 219, 219))

    SIZE = 30 # 棋盘每个点时间的间隔
    dim = 2
    arr = array
    if dim == 1:
        Line_Points_x = len(arr)        #横向上有多少个点
        Line_Points_y = 1   #纵向上有多少个点
    elif dim == 2:
        Line_Points_x = arr.shape[1]    #横向上有多少点
        Line_Points_y = arr.shape[0]    #纵向上有多上点
    Outer_Width = 20 # 棋盘外宽度
    Border_Width = 4 # 边框宽度
    Inside_Width = 20 # 边框跟实际的棋盘之间的间隔
    Line_Points = max(Line_Points_x, Line_Points_y)
    Border_Length_x = SIZE * (Line_Points_x - 1) + Inside_Width * 2 + Border_Width # 边框线的长度
    Border_Length_y = SIZE * (Line_Points_y - 1) + Inside_Width * 2 + Border_Width # 边框线的长度
    Start_X = Start_Y = Outer_Width + int(Border_Width / 2) + Inside_Width # 网格线起点（左上角）坐标
    SCREEN_HEIGHT = SIZE * (Line_Points_y - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2 # 游戏屏幕的高
    SCREEN_WIDTH = SIZE * (Line_Points_x - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2 # 游戏屏幕的宽

    Stone_Radius = SIZE // 2 - 3 # 棋子半径
    Stone_Radius2 = SIZE // 2 + 3
    Checkerboard_Color = (230, 153, 102) # 棋盘颜色
    BLACK_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    RED_COLOR = (200, 30, 30)
    BLUE_COLOR = (30, 30, 200)
    YELLOW_COLOR = (230, 153, 102)

    BLACK_STONE_COLOR = (45, 45, 45)
    WHITE_STONE_COLOR = (219, 219, 219)
    RIGHT_INFO_POS_X = SCREEN_HEIGHT + Stone_Radius2 * 2 + 10


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))

def show_board(array):
    init_parameters(array)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('壮猿五子棋')
    font1 = pygame.font.SysFont('SimHei', 36)
    font2 = pygame.font.SysFont('SimHei', 72)
    fwidth, fheight = font2.size('黑方获胜')
    checkerboard = Checkerboard(Line_Points, arr, dim
                                )
    cur_runner = BLACK_CHESSMAN
    winner = None
    while True:
        for event in pygame.event.get():              #退出
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:               #重新开局
                if event.key == K_RETURN:
                    if winner is not None:
                        winner = None
                        cur_runner = BLACK_CHESSMAN
                        checkerboard = Checkerboard(Line_Points, arr, dim)
            elif event.type == MOUSEBUTTONDOWN:
                if winner is None:
                    pressed_array = pygame.mouse.get_pressed()
                    if pressed_array[0]:              #鼠标左键按下
                        mouse_pos = pygame.mouse.get_pos()
                        click_point = _get_clickpoint(mouse_pos)   #click_point对应整数坐标
                        if click_point is not None:
                            if checkerboard.can_drop(click_point): #该位置是否可以落子
                                winner = checkerboard.drop(cur_runner, click_point)
                                if cur_runner == BLACK_CHESSMAN:
                                    cur_runner = WHITE_CHESSMAN
                                else:
                                    cur_runner = BLACK_CHESSMAN
                        else:
                            print('超出棋盘区域')
        # 画棋盘
        _draw_checkerboard(screen)

        # 画棋盘上已有的棋子
        for i, row in enumerate(checkerboard.checkerboard):
            for j, cell in enumerate(row):
                if cell == BLACK_CHESSMAN.Value:
                    _draw_chessman(screen, Point(j, i), BLACK_CHESSMAN.Color)
                elif cell == WHITE_CHESSMAN.Value:
                    _draw_chessman(screen, Point(j, i), WHITE_CHESSMAN.Color)


        if winner:
            print_text(screen, font2, (SCREEN_WIDTH - fwidth)//2, (SCREEN_HEIGHT - fheight)//2, winner.Name + '获胜', RED_COLOR)
            if cur_runner == BLACK_CHESSMAN:
                print_text(screen, font1, RIGHT_INFO_POS_X, Start_X, '获胜' if winner else '落子中', BLUE_COLOR)
            else:
                print_text(screen, font1, RIGHT_INFO_POS_X, Start_X + Stone_Radius2 * 3, '获胜' if winner else '落子中', BLUE_COLOR)
        pygame.display.flip()
# 画棋盘
def _draw_checkerboard(screen):
    # 填充棋盘背景色
    screen.fill(Checkerboard_Color)
    #screen.blit(pygame.transform.scale(image_bg, (SCREEN_WIDTH,SCREEN_HEIGHT)), (0, 0))
    # 画棋盘网格线外的边框
    pygame.draw.rect(screen, BLACK_COLOR, (Outer_Width, Outer_Width, Border_Length_x, Border_Length_y), Border_Width)
    # 画网格线
    for i in range(Line_Points_y):                                  #画横线
        pygame.draw.line(screen, BLACK_COLOR,
                        (Start_Y, Start_Y + SIZE * i),
                        (Start_Y + SIZE * (Line_Points_x - 1), Start_Y + SIZE * i),
                        1)
    for j in range(Line_Points_x):                                  #画竖线
        pygame.draw.line(screen, BLACK_COLOR,
                        (Start_X + SIZE * j, Start_X),
                        (Start_X + SIZE * j, Start_X + SIZE * (Line_Points_y - 1)),
                        1)

    #可落子处标记圆形边框
    for i in range(Line_Points_x):
        for j in range(Line_Points_y):
            pygame.gfxdraw.aacircle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, 2, BLACK_COLOR)


# 画棋子
def _draw_chessman(screen, point, stone_color):
    # pygame.draw.circle(screen, stone_color, (Start_X + SIZE * point.X, Start_Y + SIZE * point.Y), Stone_Radius)
    pygame.gfxdraw.aacircle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)       #圆形边框
    pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)  #圆形填充

def _draw_chessman_pos(screen, pos, stone_color):
    pygame.gfxdraw.aacircle(screen, pos[0], pos[1], Stone_Radius2, stone_color)
    pygame.gfxdraw.filled_circle(screen, pos[0], pos[1], Stone_Radius2, stone_color)

# 根据鼠标点击位置，返回游戏区坐标
def _get_clickpoint(click_pos):
    pos_x = click_pos[0] - Start_X      #与网格线左上角横向距离
    pos_y = click_pos[1] - Start_Y      #与网格线左上角纵向距离
    if pos_x < -Inside_Width or pos_y < -Inside_Width:
        return None
    x = pos_x // SIZE
    y = pos_y // SIZE
    if pos_x % SIZE  > Stone_Radius:
        x += 1
    if pos_y % SIZE  > Stone_Radius:
        y += 1
    if x  >= Line_Points_x or y  >= Line_Points_y:
        return None

    return Point(x, y)








