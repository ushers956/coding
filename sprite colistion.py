import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load(""),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
class sprite(pygame. sprite. Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Serface([width, height])
        self.image.fill(pygame.color('dodger blue'))
        pygame.draw.rect(self.image, color, pygame.rect(0, 0, width, height))
        self.rect = self.image.get_rect()

        def mover(self,x_change, y_change):
            self.rect.x = max(
                min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
            self.rect.y = max(
                min(self.rect.y + y_change,SCREEN_HEIGHT - self.rect.width), 0)
            
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption