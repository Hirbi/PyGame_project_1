import pygame
import os
from constants import img_folder


class Mana(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'mana.png')),
                                            (30, 60))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
