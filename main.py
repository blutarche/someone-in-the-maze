import pygame
from pygame.locals import *

import gamelib
from elements import Map, Player


class MazeGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    RED   = pygame.Color('red')

    HEIGHT = 600
    WIDTH = 900

    ROW = 41
    COLUMN = 73

    def __init__(self):
        super(MazeGame, self).__init__('Someone in the Maze', MazeGame.BLACK, window_size=(MazeGame.WIDTH, MazeGame.HEIGHT))
        self.piece_size = MazeGame.WIDTH / MazeGame.COLUMN
        self.map = Map(row=MazeGame.ROW, 
                        column=MazeGame.COLUMN, 
                        piece_size=self.piece_size)
        self.player = Player(size=self.piece_size, pos=(1,1), color=MazeGame.RED, gamemap=self.map)
        self.is_started = False

    def start_game(self):
        self.init()
        self.is_started = True

    def init(self):
        super(MazeGame, self).init()
        self.time = 0.0
        self.render_string()

    def update(self):
        self.time = pygame.time.get_ticks()/1000
        print "TIME: "+str(self.time)

    def render_string(self):
        self.render_time()

    def render_time(self):
        self.time_image = self.font.render("Time = %d" % self.time, 0,MazeGame.WHITE)

    def render(self, surface):
        self.map.render(surface)
        self.player.render(surface)
        surface.blit(self.time_image, (20, MazeGame.HEIGHT - 50))

    def on_key_up(self,key):
        if self.is_started:
            if key == K_UP:
                self.player.up()
            if key == K_DOWN:
                self.player.down()
            if key == K_LEFT:
                self.player.left()
            if key == K_RIGHT:
                self.player.right()
        else:
            if key == K_RETURN:
                self.start_game()

def main():
    game = MazeGame()
    game.run()

if __name__ == '__main__':
    main()
