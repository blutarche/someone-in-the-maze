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
        self.piece_size = piece_size

    def isplayer_cangoto(self, x, y):
        if self.map[y][x]>0:
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
        color_code = int(float(piece) / float(Map.WALK_LIMIT))*255
        color = pygame.Color(color_code, color_code, color_code);
        pygame.draw.rect(surface,
                         color,
                         pygame.Rect(x * self.piece_size,
                                     y * self.piece_size,
                                     self.piece_size,
                                     self.piece_size),
                         0)

#########################################
class Player(object):

    def __init__(self, size, color, pos, gamemap):
        (self.x, self.y) = pos
        self.color = color
        self.map = gamemap

    def up(self):
        if is_walkable(self.x, self.y - 1):
            self.y = self.y - 1

    def down(self):
        if is_walkable(self.x, self.y + 1):
            self.y = self.y + 1

    def left(self):
        if is_walkable(self.x - 1, self.y):
            self.x = self.x - 1

    def right(self):
        if is_walkable(self.x + 1, self.y):
            self.x = self.x + 1

    def is_walkable(self, x, y):
        return self.map.isplayer_cangoto(self.x, self.y)

    def render(self, surface):
        pos = (int(self.x),int(self.y))
