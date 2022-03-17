import pygame
import os
from constants import COLORS, WIDTH, HEIGHT, player_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, p_img="p1_jump.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(player_folder, p_img))
        # self.image.set_colorkey('GREEN')
        self.rect = self.image.get_rect()
        self.rect.center = x + self.rect.width / 2, y + self.rect.height / 2

    def move(self, add_x=5, add_y=5):
        if 0 <= self.rect.x + add_x <= WIDTH - self.rect.width + 1:
            self.rect.x += add_x
        if 0 <= self.rect.y + add_y <= HEIGHT - self.rect.height + 1:
            self.rect.y += add_y

    def update(self):
        pass


