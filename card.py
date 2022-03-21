import pygame
import os
import random
from constants import COLORS, CARD_SIZE_W, CARD_SIZE_H, img_folder


class Card(pygame.sprite.Sprite):
    card_picked = False

    def __init__(self, x=0, y=0, all_tables=False):
        pygame.sprite.Sprite.__init__(self)
        # установка изображения
        # self.image = pygame.Surface((CARD_SIZE_W, CARD_SIZE_H))
        self.all_tables = all_tables
        self.image = pygame.image.load(os.path.join(img_folder, 'cards', 'fon.png'))
        self.text_ramka_img = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', 'ramkatext.png')),
                                               (CARD_SIZE_W, CARD_SIZE_H))
        # self.image = pygame.transform.scale(self.image, (CARD_SIZE_W, CARD_SIZE_H))
        # self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pygame.draw.rect(self.image, COLORS["BLACK"], pygame.Rect(0, 0, CARD_SIZE_W, CARD_SIZE_H), 4)
        self.image.blit(self.text_ramka_img, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def is_in(self, x, y):
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def clear(self):
        self.rect.center = 100, 100

    def move_card(self, add_x, add_y):
        self.rect.x += add_x
        self.rect.y += add_y

    def set_cords(self, add_x, add_y):
        self.rect.x = add_x
        self.rect.y = add_y

    def set_surface(self, surface):
        surface.blit(self.image, (2, 2))

    def get_hp(self):
        return 1


