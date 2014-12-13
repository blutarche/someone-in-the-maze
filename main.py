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
        super(MazeGame, self).__init__('3 minutes MAZE', MazeGame.BLACK, window_size=(MazeGame.WIDTH, MazeGame.HEIGHT))
        self.piece_size = MazeGame.WIDTH / MazeGame.COLUMN
        self.map = Map(row=MazeGame.ROW, 
                        column=MazeGame.COLUMN, 
                        piece_size=self.piece_size)
        self.player = Player(size=self.piece_size, pos=(1,1), color=MazeGame.RED, gamemap=self.map)
        self.is_started = False
        self.is_end = False
        self.last_ticks = 0

    def start_game(self):
        self.init()
        self.is_started = True
        self.is_end = False

    def init(self):
        super(MazeGame, self).init()
        self.time = 180999
        self.render_string()

    def update(self):
        self.update_time()
        self.render_time()

    def update_time(self):
        this_tick = pygame.time.get_ticks()
        if self.is_started:
            self.time -= this_tick - self.last_ticks
        else:
            pass
        self.last_ticks = this_tick

    def render_string(self):
        self.render_time()

    def render_time(self):
        time_in_sec = self.time/1000
        seconds = time_in_sec % 60
        minutes = time_in_sec / 60
        self.time_image = self.font.render("Time %d:%02d" % (minutes, seconds), 0, MazeGame.WHITE)

    def render(self, surface):
        if self.is_started:
            self.render_game(surface)
        elif self.is_end:
            self.render_gameover(surface)
        else:
            self.render_start(surface)

    def render_game(self, surface):
        self.map.render(surface)
        self.player.render(surface)
        surface.blit(self.time_image, (20, MazeGame.HEIGHT - 50))

    def render_gameover(self, surface):
        pass

    def render_start(self, surface):
        pass

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
            if key == K_SPACE:
                print "Game start!"
                self.start_game()

def main():
    game = MazeGame()
    game.run()

if __name__ == '__main__':
    main()
