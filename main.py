import pygame

from gamemode import Gamemode
from player import Player

playerCount = 4

pygame.init()

pygame.display.set_caption("Working With Rectangles")

gm = Gamemode()
gm.run()
pygame.quit()
