import pygame
from pygame.locals import *

from maze_algo import make_maze

class Map(object):

    def __init__(self, wall_color, passage_color, row, column, piece_size):
        self.row = row
        self.column = column
        self.map = make_maze(w=(column-1)/2, h=(row-1)/2)
        self.wall_color = wall_color
        self.passage_color = passage_color
        self.piece_size = piece_size

    def render(self, surface):
        y = -0.5
        for row in self.map:
            x = 0.5
            for piece in row:
                self.render_piece(surface, x, y, piece)
                x = x + 1
            y = y + 1

    def render_piece(self, surface, x, y, piece):
        color = 0
        if piece == '#':
            color = self.wall_color
        elif piece == ' ':
            color = self.passage_color
        pygame.draw.rect(surface,
                         color,
                         pygame.Rect(x * self.piece_size,
                                     y * self.piece_size,
                                     self.piece_size,
                                     self.piece_size),
                         0)



class Player(object):

    def __init__(self, size, color, pos)
        pass



class Ball(object):

    def __init__(self, radius, color, pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def bounce_player(self):
        self.vx = abs(self.vx) # bounce ball back
        
    def move(self, delta_t, display, player):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t

        # make ball bounce if hitting wall
        if self.x < self.radius:
            self.vx = abs(self.vx)
            game_over = True # game over when ball hits left wall
        if self.y < self.radius:
            self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self, pos, color, width=100):
        self.width = width
        self.pos = pos
        self.color = color

    def can_hit(self, ball):
        return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
            and ball.x-ball.radius < self.THICKNESS

    def move_up(self):
        self.pos -= 5

    def move_down(self):
        self.pos += 5

    def render(self, surface):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(0,
                                     self.pos - self.width/2.0,
                                     self.THICKNESS,
                                     self.width),
                         2)
        
'''