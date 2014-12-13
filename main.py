import pygame
from pygame.locals import *

import gamelib
from elements import Map, Player


class MazeGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    RED   = pygame.Color('red')

    ROW = 31
    COLUMN = 63

    HEIGHT = 700
    WIDTH = 1300

    TIME = 120000

    def __init__(self):
        super(MazeGame, self).__init__('Collapsing Maze', MazeGame.BLACK, window_size=(MazeGame.WIDTH, MazeGame.HEIGHT))
        self.piece_size = MazeGame.WIDTH / MazeGame.COLUMN
        self.is_started = False
        self.is_lose = False
        self.is_win = False
        self.last_ticks = 0
        self.time_win = 0

    def start_game(self):
        self.init()
        self.is_started = True
        self.is_lose = False
        self.is_win = False

    def init(self):
        super(MazeGame, self).init()
        self.time = MazeGame.TIME + 999
        self.map = Map(row=MazeGame.ROW, 
                        column=MazeGame.COLUMN, 
                        piece_size=self.piece_size)
        self.player = Player(size=self.piece_size, pos=(1, 1), color=MazeGame.RED, gamemap=self.map)

    def update(self):
        if self.is_started:
            self.update_time()
            self.check_finish()

    def update_time(self):
        this_tick = pygame.time.get_ticks()
        self.time -= this_tick - self.last_ticks
        self.last_ticks = this_tick

    def check_finish(self):
        if self.time <= 0:
            self.is_lose = True
            self.is_started = False
        elif self.player.is_atgoal():
            self.time_win = 180000 - self.time
            self.is_win = True
            self.is_started = False

    def render(self, surface):
        self.render_time()
        if self.is_started:
            self.render_game(surface)
        elif self.is_lose:
            self.render_gameover(surface)
        elif self.is_win:
            self.render_win(surface)
        else:
            self.render_start(surface)

    def render_time(self):
        time_in_sec = self.time/1000
        seconds = time_in_sec % 60
        minutes = time_in_sec / 60
        self.time_image = self.font.render("%d:%02d" % (minutes, seconds), 0, MazeGame.WHITE)

    def render_game(self, surface):
        self.map.render(surface)
        self.player.render(surface)
        surface.blit(self.time_image, (MazeGame.WIDTH/2 - 25, MazeGame.HEIGHT - 50))

    def render_gameover(self, surface):
        surface.fill((255,128,128))
        self.render_message(surface, "YOU LOSE!", 60, 70)
        self.render_message(surface, "You didn't finished maze", 147, 50)
        self.render_message(surface, "Press Space to restart", 135, -40)

    def render_win(self, surface):
        surface.fill((128,255,128))
        time_in_sec = (MazeGame.TIME - self.time)/1000
        seconds = time_in_sec % 60
        minutes = time_in_sec / 60
        self.render_message(surface, "Congratulation!", 90, 70)
        self.render_message(surface, "You finished maze in", 125, 50)
        self.render_message(surface, "%d:%02d" % (minutes, seconds), 25, 10)
        self.render_message(surface, "Press Space to restart", 135, -40)

    def render_message(self, surface, message, x, y):
        self.message_image = self.font.render(message, 0, MazeGame.BLACK)
        surface.blit(self.message_image, (MazeGame.WIDTH/2 - x, MazeGame.HEIGHT/2 - y))

    def render_start(self, surface):
        self.greeting_image = self.font.render("Press Space to start", 0, MazeGame.WHITE)
        surface.blit(self.greeting_image, (MazeGame.WIDTH/2 - 120, MazeGame.HEIGHT/2 - 10))

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
