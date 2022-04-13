import pygame
from card import Card
import os
import random
from constants import COLORS, CARD_SIZE_W, CARD_SIZE_H, CARD_TYPES, img_folder, all_sprites, font


class MobCard(Card):

    # хп, дамаг, стоимость, тип(0 - для всех), координаты х и у
    def __init__(self, hp=0, dp=0, cost=0, kind=0, mob_img="monke.png", all_tables=False, x=0, y=0):
        super().__init__(x, y, all_tables)
        self.hp, self.dp, self.cost, self.kind = hp, dp, cost, kind
        # установка рамок
        self.ramka_up = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', 'ramkaup.png')),
                                               (CARD_SIZE_W, CARD_SIZE_H))
        self.ramka_down = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', 'ramkadown.png')),
                                                 (CARD_SIZE_W, CARD_SIZE_H))
        self.mob_img = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', mob_img)),
                                              (CARD_SIZE_W - 20, CARD_SIZE_W - 20))
        self.image.blit(self.mob_img, (4, 2))
        self.image.blit(self.ramka_up, (0, 0))
        self.image.blit(self.ramka_down, (0, 0))
        move_x, move_y = 12, 15
        # установка хп
        self.text_hp = font.render(str(self.hp), True, COLORS['WHITE'])
        self.hp_rect = self.text_hp.get_rect()
        self.hp_rect.center = CARD_SIZE_W - move_x, CARD_SIZE_H - move_y
        self.image.blit(self.text_hp, self.hp_rect)
        # установка урона
        self.text_dp = font.render(str(self.dp), True, COLORS['WHITE'])
        self.dp_rect = self.text_dp.get_rect()
        self.dp_rect.center = move_x, CARD_SIZE_H - move_y
        self.image.blit(self.text_dp, self.dp_rect)
        # установка стоимости
        self.text_cost = font.render(str(self.cost), True, COLORS['WHITE'])
        self.cost_rect = self.text_cost.get_rect()
        self.cost_rect.center = CARD_SIZE_W - move_x, move_y + 2
        self.image.blit(self.text_cost, self.cost_rect)
        # Установка типа
        # 1 - floppa, 2 = robert
        self.text_kind = font.render(str(self.kind), True, CARD_TYPES[self.kind])
        self.kind_rect = self.text_kind.get_rect()
        self.kind_rect.center = move_x, move_y + 2
        self.image.blit(self.text_kind, self.kind_rect)

    def get_hp(self):
        return self.hp
