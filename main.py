import pygame
from pygame.locals import *

import gamelib
from elements import Map, Player


class MazeGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')

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
        self.player = Player(size=self.piece_size, pos=(1,1), color=MazeGame.GREEN, gamemap=self.map)
        self.time = 0


    def init(self):
        super(MazeGame, self).init()

    def update(self):
        pass

    def render_score(self):
        pass

    def render(self, surface):
        self.map.render(surface)

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

def main():
    game = MazeGame()
    game.run()

if __name__ == '__main__':
    main()
