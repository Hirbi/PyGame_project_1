import pygame
import os
import random
from constants import COLORS, WIDTH, HEIGHT, player_folder


class Card(pygame.sprite.Sprite):
    def __init__(self, surface, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 150))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        surface.blit(self.image, (5, 5))
        print(self.image.get_rect().width)
        # self.rect.center = x, y

    def is_in(self, x, y):
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def set_cords(self, add_x, add_y):
        self.rect.x += add_x
        self.rect.y += add_y
        print('HZ')

    def set_surface(self, surface):
        surface.blit(self.image, (2, 2))
