import pygame
import sys
from pygame.locals import *
import traceback
import people
import wall
import random
import numpy as np
import maze
import util
from queue import Queue

a = []

def bfs(pos):

    # 创建队列
    q = Queue()

    # 将根节点加入队列
    q.put(pos)

    # 如果队列不为空
    while q.qsize() != 0:

        # 获取节点（出队）
        pos = q.get()

        # 存储查找到的节点
        a.append(pos)

        # 判断是否找到出口，找到则退出bfs()
        if check_exit(pos):
            return

        # 如果上方可走，入队
        if check_up(pos):
            q.put(get_up(pos))

        # 如果右方可走，入队
        if check_right(pos):
            q.put(get_right(pos))

        # 如果下方可走，入队
        if check_down(pos):
            q.put(get_down(pos))

        # 如果左方可走，入队
        if check_left(pos):
            q.put(get_left(pos))

















# ----------------以下代码为封装代码部分，不需要修改-------------------------
pygame.init()
size = width, height = 960, 672
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("迷宫探路仪")
back = (0, 0, 0)
level = 1

def main():
    global a, maze_copy, exitdoor, flag
    clock = pygame.time.Clock()
    Gamestate = 0
    # 字体设置
    start_icon = pygame.image.load('images/background/start.png').convert_alpha()
    start_icon_rect = start_icon.get_rect()
    start_icon_rect.center = (width / 2 - 10, height / 2 + 20)

    text_font1 = pygame.font.SysFont('arial', 30)
    text_bfs = text_font1.render(u'BFS searching', True, (255, 255, 255))
    text_bfs_rect = text_bfs.get_rect()
    text_bfs_rect.center = (width - 145, 100)


    image_startmenu = pygame.image.load('images/background/background.png')  # 开始界面背景图
    image_background = pygame.image.load('images/background/bg.png')  # 游戏界面背景图
    image_path = pygame.image.load("images/wall/path.png").convert_alpha()  # .convert_alpha提升blit速度
    dead_end = pygame.image.load("images/wall/destroyed.png").convert_alpha()

    maze_size = 10

    Maze = maze.createmaze(maze_size)

    # 判定生成的迷宫能否用DFS走通，如果不能，重新生成一个迷宫。
    while util.solution_maze(Maze, 'DFS') == False:
        Maze = maze.createmaze(maze_size)

    wall_location = []
    for i in range(2 * maze_size + 1):
        for j in range(2 * maze_size + 1):
            # 存储墙壁的位置坐标
            if Maze[i][j] == 0:
                wall_location.append((i, j))
            # 人物的位置坐标
            elif Maze[i][j] == 10:
                position_people = i * 32, j * 32
            # 宝藏的位置坐标
            elif Maze[i][j] == 1:
                position_treasure = i * 32, j * 32

    me = people.People(position_people)

    walls = []
    for each in wall_location:
        position = each[0] * 32, each[1] * 32
        wa = wall.Wall(position, 0)
        walls.append(wa)

    treasure = pygame.image.load('images/wall/treasure.png')
    treasure_rect = treasure.get_rect()
    treasure_rect.left = position_treasure[0]
    treasure_rect.top = position_treasure[1]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if Gamestate == 0: # 起始界面
            if event.type == MOUSEBUTTONDOWN:

                # 检测左键是否按下。
                # 同时检测点击处是否在start图标内。
                if event.button == 1 and start_icon_rect.collidepoint(event.pos):
                    Gamestate = 1
            screen.blit(image_startmenu, (0, 0))
            screen.blit(start_icon, start_icon_rect)

        if Gamestate == 1: # 游戏界面
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text_bfs_rect.collidepoint(event.pos):
                    Gamestate = 2

            screen.fill(bg)
            screen.blit(image_background, (0, 0))
            screen.blit(treasure, treasure_rect)
            for each in walls:
                screen.blit(each.image1, each.rect)

            screen.blit(me.people, me.rect)
            screen.blit(text_bfs, text_bfs_rect)

        if Gamestate == 2:  # 广度优先搜索

            # 坐标模式转换为数组模式

            maze_copy = np.zeros((maze_size*2+1, maze_size*2+1))
            for i in range(maze_size*2+1):
                for j in range(maze_size*2+1):
                    maze_copy[i][j] = Maze[j][i]


            start = (np.where(maze_copy == 10)[0][0], np.where(maze_copy == 10)[1][0])
            exitdoor = (np.where(maze_copy == 1)[0][0], np.where(maze_copy == 1)[1][0])
            pos = start

            bfs(pos)


            visited_path = []
            step_b = 0
            for point in a:
                visited_path.append([point[1], point[0]])
                screen.fill(bg)
                screen.blit(image_background, (0, 0))
                screen.blit(treasure, treasure_rect)
                screen.blit(text_bfs, text_bfs_rect)
                step_res_b = text_font1.render('Step:     ' + str(step_b).zfill(3), True, (255, 255, 255))
                screen.blit(step_res_b, (730, 460))
                step_b += 1

                for each in walls:
                    screen.blit(each.image1, each.rect)
                for path in visited_path:
                    screen.blit(image_path, (path[0] * 32, path[1] * 32))
                me.rect.left = 32 * point[1]
                me.rect.top = 32 * point[0]
                screen.blit(me.people, me.rect)
                pygame.display.flip()
                pygame.time.wait(300)

            me.rect.left = 32 * a[0][1]
            me.rect.top = 32 * a[0][0]
            pygame.time.wait(1000)
            Gamestate = 1


        pygame.display.flip()
        clock.tick(60)


def check_exit(pos):
    if pos == exitdoor:
        return True
    else:
        return False


def check_up(pos):
    if maze_copy[pos[0] - 1][pos[1]] != 0 and (pos[0] - 1, pos[1]) not in a:
        return True
    else:
        return False


def get_up(pos):
    return (pos[0] - 1, pos[1])


def check_down(pos):
    if maze_copy[pos[0] + 1][pos[1]] != 0 and (pos[0] + 1, pos[1]) not in a:
        return True
    else:
        return False


def get_down(pos):
    return (pos[0] + 1, pos[1])


def check_left(pos):
    if maze_copy[pos[0]][pos[1] - 1] != 0 and (pos[0], pos[1] - 1) not in a:
        return True
    else:
        return False


def get_left(pos):
    return (pos[0], pos[1] - 1)


def check_right(pos):
    if maze_copy[pos[0]][pos[1] + 1] != 0 and (pos[0], pos[1] + 1) not in a:
        return True
    else:
        return False


def get_right(pos):
    return (pos[0], pos[1] + 1)


if __name__ == "__main__":
    main()

