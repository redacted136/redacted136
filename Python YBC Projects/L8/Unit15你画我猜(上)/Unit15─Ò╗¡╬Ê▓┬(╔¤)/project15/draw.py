import pygame
from pygame.locals import *
import math


# 画笔
class Brush:
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 10
        self.drawing = False
        self.last_pos = None
        self.style = True
        self.brush = pygame.image.load("images/brush.png").convert_alpha()
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))

    def start_draw(self, pos):
        self.drawing = True
        self.last_pos = pos

    def end_draw(self):
        self.drawing = False

    def set_brush_style(self, style):
        print("* set brush style to", style)
        self.style = style

    def get_brush_style(self):
        return self.style

    def get_current_brush(self):
        return self.brush_now

    def set_size(self, size):
        if self.style == True :
            pass
        else:
            if size < 1:
                size = 1
            elif size > 30:
                size = 30
            print("* set brush size to", size)
            self.size = size
            if self.size >= 30:
                self.brush_now = self.brush.subsurface((0, 0), (30 * 2, 30 * 2))
            else: self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))

    def get_size(self):
        return self.size

    def set_color(self, color):
        self.color = color
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                self.brush.set_at((i, j),
                                  color + (self.brush.get_at((i, j)).a,))

    def get_color(self):
        return self.color

    def draw(self, pos):
        if self.drawing:
            for p in self._get_points(pos):
                if self.style:
                    self.screen.blit(self.brush_now, p)
                else:
                    pygame.draw.circle(self.screen, self.color, p, self.size)
            self.last_pos = pos

    def _get_points(self, pos):
        points = [(self.last_pos[0], self.last_pos[1])]
        len_x = pos[0] - self.last_pos[0]
        len_y = pos[1] - self.last_pos[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in range(int(length)):
            points.append((points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)
        return list(set(points))

# 左侧菜单栏
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.brush = None
        self.colors = [    #颜色按钮
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80),
        ]
        self.colors_rect = []
        for (i, rgb) in enumerate(self.colors):
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)
            self.colors_rect.append(rect)

        self.pens = [     #画笔按钮
            pygame.image.load("images/pen1.png").convert_alpha()
            # pygame.image.load("images/pen1.png").convert_alpha()
        ]
        self.pens_rect = []
        for (i, img) in enumerate(self.pens):
            rect = pygame.Rect(10, 10 + i * 64, 64, 64)
            self.pens_rect.append(rect)

        self.sizes = [    #调整笔画粗心按钮
            pygame.image.load("images/big.png").convert_alpha(),
            pygame.image.load("images/small.png").convert_alpha()
        ]
        self.sizes_rect = []
        for (i, img) in enumerate(self.sizes):
            rect = pygame.Rect(10 + i * 32, 138, 32, 32)
            self.sizes_rect.append(rect)

        self.clear_button = [   #清屏按钮
            pygame.image.load("images/clear.png").convert_alpha()
        ]
        self.clear_rect = []
        for (i, img) in enumerate(self.clear_button):
            rect = pygame.Rect(10 + i * 32, 80, 50, 50)
            self.clear_rect.append(rect)

        self.save_button = [       #保存按钮
            pygame.image.load("images/save.png").convert_alpha()
        ]
        self.save_rect = []
        for (i, img) in enumerate(self.save_button):
            rect = pygame.Rect(10 + i * 32, 530, 50, 50)
            self.save_rect.append(rect)

    def set_brush(self, brush):
        self.brush = brush

    def draw(self):
        for (i, img) in enumerate(self.pens):
            self.screen.blit(img, self.pens_rect[i].topleft)

        for (i, img) in enumerate(self.sizes):
            self.screen.blit(img, self.sizes_rect[i].topleft)

        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        if self.brush.get_brush_style():
            x = x - size
            y = y - size
            self.screen.blit(self.brush.get_current_brush(), (x, y))

        else:
            pygame.draw.circle(self.screen,
                               self.brush.get_color(), (x, y), size)

        for (i, rgb) in enumerate(self.colors):
            pygame.draw.rect(self.screen, rgb, self.colors_rect[i])

        for (i, img) in enumerate(self.clear_button):
            self.screen.blit(img, self.clear_rect[i].topleft)

        for (i, img) in enumerate(self.save_button):
            self.screen.blit(img, self.save_rect[i].topleft)

    def click_button(self, pos):
        for (i, rect) in enumerate(self.pens_rect):
            if rect.collidepoint(pos):
                self.brush.set_brush_style(bool(i))
                return True
        for (i, rect) in enumerate(self.sizes_rect):   #调整笔画粗细
            if rect.collidepoint(pos):
                if i:
                    self.brush.set_size(self.brush.get_size() - 1)
                else:
                    self.brush.set_size(self.brush.get_size() + 1)
                return True
        for (i, rect) in enumerate(self.colors_rect):  #换颜色
            if rect.collidepoint(pos):
                if self.brush.style == True:
                    return True
                self.brush.set_color(self.colors[i])
                return True

        for (i, rect) in enumerate(self.clear_rect):  #清屏
            if rect.collidepoint(pos):
                self.screen.fill((255, 255, 255))
                return True

        for (i, rect) in enumerate(self.save_rect):
            if rect.collidepoint(pos):
                size = (720, 590)
                img = pygame.Surface(size)
                img.blit(self.screen, (0, 0), ((80, 0), size))

                pygame.image.save(img, "screenshot.jpg")


                return True

        return False




class Painter:     #运行画板
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Painter")
        self.clock = pygame.time.Clock()
        self.brush = Brush(self.screen)
        self.menu = Menu(self.screen)
        self.menu.set_brush(self.brush)



    def run(self):
        self.screen.fill((255, 255, 255))
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen.fill((255, 255, 255))
                elif event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] <= 74 and self.menu.click_button(event.pos):
                        pass
                    else:
                        self.brush.start_draw(event.pos)
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.brush.end_draw()
            self.menu.draw()
            pygame.display.update()


def main():
    app = Painter()
    app.run()


if __name__ == '__main__':
    main()