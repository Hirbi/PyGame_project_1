import pygame
from card import Card
import random
from constants import COLORS, CARD_SIZE_W, CARD_SIZE_H, CARD_TYPES

font = pygame.font.Font(None, 30)


class MobCard(Card):

    # хп, дамаг, стоимость, тип(0 - для всех), координаты х и у
    def __init__(self, hp=0, dp=0, cost=0, kind=0, x=0, y=0):
        super().__init__(x, y)
        self.hp, self.dp, self.cost, self.kind = hp, dp, cost, kind
        # установка всех углов
        # установка хп
        self.text_hp = font.render(str(self.hp), True, COLORS['RED'])
        self.hp_rect = self.text_hp.get_rect()
        self.hp_rect = CARD_SIZE_W - self.hp_rect.width, CARD_SIZE_H - self.hp_rect.height
        self.image.blit(self.text_hp, self.hp_rect)
        # установка урона
        self.text_dp = font.render(str(self.dp), True, COLORS['WHITE'])
        self.dp_rect = self.text_dp.get_rect()
        self.dp_rect = 0, CARD_SIZE_H - self.dp_rect.height
        self.image.blit(self.text_dp, self.dp_rect)
        # установка стоимости
        self.text_cost = font.render(str(self.cost), True, COLORS['BLUE'])
        self.cost_rect = self.text_cost.get_rect()
        self.cost_rect = CARD_SIZE_W - self.cost_rect.width, 0
        self.image.blit(self.text_cost, self.cost_rect)
        # Установка типа
        self.text_kind = font.render(str(self.kind), True, CARD_TYPES[self.kind])
        self.kind_rect = self.text_kind.get_rect()
        self.kind_rect = 0, 0
        self.image.blit(self.text_kind, self.kind_rect)
