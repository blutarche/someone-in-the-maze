import pygame
from pygame.locals import *

from maze_algo import make_maze

class Map(object):

    WALK_LIMIT = 5

    def __init__(self, row, column, piece_size):
        self.row = row
        self.column = column
        self.map = make_maze(walk_limit=Map.WALK_LIMIT,
                            w=(column-1)/2, 
                            h=(row-1)/2)
        self.map[row-2][column-2] = -1
        self.piece_size = piece_size

    def walkto(self, x, y, before_x, before_y):
        if self.map[y][x]>0:
            self.map[before_y][before_x] -= 1
            return True
        else:
            return False

    def render(self, surface):
        y = 1
        for row in self.map:
            x = 1
            for piece in row:
                self.render_piece(surface, x, y, piece)
                x = x + 1
            y = y + 1

    def render_piece(self, surface, x, y, piece):
        s = pygame.Surface((self.piece_size, self.piece_size))
        if piece != -1:
            color_code = int(float(piece)*255 / float(Map.WALK_LIMIT))
            s.set_alpha(color_code)
            s.fill((255,255,255))
        else:
            s.set_alpha(255)
            s.fill((0,200,0))
        surface.blit(s, (x * self.piece_size, y * self.piece_size)) 

#########################################
class Player(object):

    def __init__(self, size, color, pos, gamemap):
        (self.x, self.y) = pos
        self.color = color
        self.map = gamemap
        self.size = size

    def up(self):
        if self.is_walkable(self.x, self.y - 1, self.x, self.y):
            self.y = self.y - 1

    def down(self):
        if self.is_walkable(self.x, self.y + 1, self.x, self.y):
            self.y = self.y + 1

    def left(self):
        if self.is_walkable(self.x - 1, self.y, self.x, self.y):
            self.x = self.x - 1

    def right(self):
        if self.is_walkable(self.x + 1, self.y, self.x, self.y):
            self.x = self.x + 1

    def is_walkable(self, x, y, before_x, before_y):
        print "Walk from (%d,%d) to (%d,%d)" % (before_x, before_y, x ,y)
        return self.map.walkto(x, y, before_x, before_y)

    def render(self, surface):
        x = self.x + 1
        y = self.y + 1
        radius = self.size / 2
        pos_render = (x*self.size + radius , y*self.size + radius)
        pygame.draw.circle(surface, self.color, pos_render, radius, 0)
