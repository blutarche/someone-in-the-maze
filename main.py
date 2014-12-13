import pygame
from pygame.locals import *

import gamelib

class MazeGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(MazeGame, self).__init__('Squash', MazeGame.BLACK)


    def init(self):
        super(MazeGame, self).init()

    def update(self):
        pass

    def render_score(self):
        pass

    def render(self, surface):
        pass

def main():
    game = MazeGame()
    game.run()

if __name__ == '__main__':
    main()
