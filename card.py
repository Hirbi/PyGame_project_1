import pygame
import os
import random
from constants import COLORS, WIDTH, HEIGHT, player_folder


class Card(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 150))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        print(self.image.get_rect().width)
        self.rect.center = x, y

    def is_in(self, x, y):
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def set_coords(self, add_x, add_y):
        self.rect.x += add_x
        self.rect.y += add_y
