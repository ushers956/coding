import pygame
import random

pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.color('blue')
LIGHTBLUE = pygame.color('lightblue')
DARKBLUE = pygame.color('darkblue')

YELLOW = pygame.color('yellow')
MAGENTA = pygame.color('magenta')
ORANGE = pygame.color('orange')
WHITE = pygame.color('white')


class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):

       super().__init__()

       self.image = pygame.surface([width, height])
       self.image.fill(color)

       self.rect = self.image.get_rect()

       self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):

        self.rect.move_ip(self.velocity)

        bountry_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            bountry_hit = True