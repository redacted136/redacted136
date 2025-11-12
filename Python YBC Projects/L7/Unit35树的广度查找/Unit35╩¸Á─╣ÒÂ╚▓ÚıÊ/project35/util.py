import numpy as np
import queue

class Maze_unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def solution_maze(maze,method):
    maze_size = maze.shape[0]
    start = (np.where(maze==10)[0][0],np.where(maze==10)[1][0])  #获取起始点坐标(i, j)
    treasure = (np.where(maze==1)[0][0],np.where(maze==1)[1][0]) #获得宝藏坐标(i, j)
    solution = []
    visited = np.zeros((maze_size,maze_size))   #经过的点数组

    if method == 'DFS':
        stack = []
        temp = Maze_unit(start[0], start[1])
        stack.append(temp)
        while stack:
            temp = stack.pop()
            solution.append([temp.x,temp.y])  #solution列表中加入目前点坐标。
            visited[temp.x,temp.y] = 1   #经过的点值设为1

            #如果找到宝藏，把经过的路径坐标存入solution_real列表中。
            #返回路径坐标。。。
            if temp.x == treasure[0] and temp.y == treasure[1]:
                solution_real = []
                for li in solution:
                    if li not in solution_real:
                        solution_real.append(li)
                return solution_real

            #可以向上走（上面没走过且没墙壁）
            if visited[temp.x-1,temp.y] == 0 and maze[temp.x-1,temp.y] != 0:
                #路径距离累加（考虑了冰面，不考虑冰面累加1就行，不用这么麻烦）
                temp_lx = Maze_unit(temp.x-1, temp.y)
                stack.append(temp_lx)

            #可以向下走
            if visited[temp.x+1,temp.y] == 0 and maze[temp.x+1,temp.y] != 0:
                temp_rx = Maze_unit(temp.x+1, temp.y)
                stack.append(temp_rx)

            #可以向左走
            if visited[temp.x,temp.y-1] == 0 and maze[temp.x,temp.y-1] != 0:
                temp_uy = Maze_unit(temp.x, temp.y-1)
                stack.append(temp_uy)

            # 可以向右走
            if visited[temp.x,temp.y+1] == 0 and maze[temp.x,temp.y+1] != 0:
                temp_dy = Maze_unit(temp.x, temp.y+1)
                stack.append(temp_dy)

        return False
        
    elif method == 'BFS':
        q = queue.Queue()
        temp = Maze_unit(start[0], start[1])
        q.put(temp)
        while q:
            temp = q.get()
            solution.append([temp.x,temp.y])
            visited[temp.x,temp.y] = 1
            if temp.x == treasure[0] and temp.y == treasure[1]:
                solution_real = []
                for li in solution:
                    if li not in solution_real:
                        solution_real.append(li)
                return solution_real
            if visited[temp.x-1,temp.y] == 0 and maze[temp.x-1,temp.y] != 0:
                temp_lx = Maze_unit(temp.x-1, temp.y)
                q.put(temp_lx)

            if visited[temp.x+1,temp.y] == 0 and maze[temp.x+1,temp.y] != 0:
                temp_rx = Maze_unit(temp.x+1, temp.y)
                q.put(temp_rx)

            if visited[temp.x,temp.y-1] == 0 and maze[temp.x,temp.y-1] != 0:
                temp_uy = Maze_unit(temp.x, temp.y-1)
                q.put(temp_uy)

            if visited[temp.x,temp.y+1] == 0 and maze[temp.x,temp.y+1] != 0:
                temp_dy = Maze_unit(temp.x, temp.y+1)
                q.put(temp_dy)

        return False



















