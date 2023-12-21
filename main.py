import pygame

from gamemode import Gamemode
from player import Player

pygame.init()

pygame.display.set_caption("Working With Rectangles")

gm = Gamemode()
gm.run()
pygame.quit()
