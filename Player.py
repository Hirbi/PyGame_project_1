import pygame
import os
from constants import COLORS, WIDTH, HEIGHT, player_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, p_img="p1_jump.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(player_folder, p_img))
        self.rect = self.image.get_rect()
        self.hand = []
        self.table = []
        self.mana = 0
        self.hp = 30
        self.rect.center = WIDTH - self.rect.width, HEIGHT - self.rect.height / 2

    def your_turn(self):
        self.rect.center = WIDTH - self.rect.width, HEIGHT - self.rect.height / 2

    def enemy_turn(self):
        self.rect.center = WIDTH - self.rect.width, self.rect.height / 2 + 4

    def get_cards(self, *card_list):
        self.hand.copy(card_list)

    def update(self):
        # self.move()
        pass

    def new_turn(self):
        self.mana = (self.mana + 1) % 10


