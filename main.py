import pygame
from pygame.locals import *


class KnockerGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(KnockerGame, self).__init__('Squash', KnockerGame.BLACK)


    def init(self):
        super(KnockerGame, self).init()

    def update(self):
        
    def render_score(self):

    def render(self, surface):

def main():
    game = KnockerGame()
    game.run()

if __name__ == '__main__':
    main()
