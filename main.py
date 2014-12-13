import pygame
from pygame.locals import *

import gamelib
from elements import Map


class MazeGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')

    HEIGHT = 600
    WIDTH = 900

    ROW = 20
    COLUMN = 36

    def __init__(self):
        super(MazeGame, self).__init__('Someone in the Maze', MazeGame.BLACK, window_size=(MazeGame.WIDTH, MazeGame.HEIGHT))
        self.piece_size = MazeGame.WIDTH / MazeGame.COLUMN
        self.map = Map(wall_color=MazeGame.BLACK, 
                        passage_color=MazeGame.WHITE, 
                        row=MazeGame.ROW, 
                        column=MazeGame.COLUMN, 
                        piece_size=self.piece_size);


    def init(self):
        super(MazeGame, self).init()

    def update(self):
        pass

    def render_score(self):
        pass

    def render(self, surface):
        self.map.render(surface)

def main():
    game = MazeGame()
    game.run()

if __name__ == '__main__':
    main()
