import pygame

from map import Map
from player import Player


class Gamemode:
    def __init__(self):
        self.players = []
        self.drops = []
        self.bombs = []

        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 400

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.map = Map()

        self.clock = pygame.time.Clock()

        self.player = Player()

    def run(self):
        run = True
        while run:


            #refresh the screen at 60 FPS
            self.clock.tick(60)

            #fill the background white
            self.screen.fill((255, 255, 255))

            self.player.move()

            self.player.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #refresh display
            pygame.display.flip()


