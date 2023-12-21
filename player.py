import pygame


class Player:
    def __init__(self):
        self.location = [0,0]
        self.stats = []
        self.cooldown = []
        self.color = [23,43,13]
        self.lives = []


        self.soldier = pygame.image.load("soldier.png").convert_alpha()

        self.rect_2 = self.soldier.get_rect()

        self.rect_2.topleft = (200, 200)

    def move(self):
        #player controls
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            self.rect_2.x -= 5
        if key[pygame.K_d] == True:
            self.rect_2.x += 5
        if key[pygame.K_w] == True:
            self.rect_2.y -= 5
        if key[pygame.K_s] == True:
            self.rect_2.y += 5

    def draw(self,screen):
        #draw the rectangle and soldier image
        pygame.draw.rect(screen, (0, 255, 255), self.rect_2)
        screen.blit(self.soldier, self.rect_2)
