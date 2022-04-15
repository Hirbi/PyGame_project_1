import pygame
from card import Card
import os
import random
from constants import COLORS, CARD_SIZE_W, CARD_SIZE_H, CARD_TYPES, img_folder, all_sprites, font, player_folder


class MobCard(Card):

    # хп, дамаг, стоимость, тип(0 - для всех), координаты х и у
    def __init__(self, hp=0, dp=0, cost=0, kind=0, mob_img="monke.png", all_tables=False, x=0, y=0):
        super().__init__(x, y, all_tables)
        self.hp, self.dp, self.cost, self.kind = hp, dp, cost, kind
        # установка рамок
        self.frame_up = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', 'ramkaup.png')),
                                               (CARD_SIZE_W, CARD_SIZE_H))
        self.frame_down = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', 'ramkadown.png')),
                                                 (CARD_SIZE_W, CARD_SIZE_H))
        self.mob_img = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cards', mob_img)),
                                              (CARD_SIZE_W - 20, CARD_SIZE_W - 20))
        self.move_x, self.move_y = 12, 15
        self.hp_color = COLORS["WHITE"]
        self.draw_all()

    def draw_all(self):
        self.draw_frame()
        self.draw_hp(self.hp)
        self.draw_damage(self.dp)
        self.draw_cost(self.cost)
        self.draw_kind(self.kind)

    # отрисовка рамки
    def draw_frame(self):
        self.image.blit(self.mob_img, (4, 2))
        self.image.blit(self.frame_up, (0, 0))
        # self.image.blit(self.frame_down, (0, 0))

    # отрисовка хр
    def draw_hp(self, hp):
        self.heart = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, 'hp.png')),
                                            (CARD_SIZE_W / 4, CARD_SIZE_W / 4))
        self.heart_rect = self.heart.get_rect()
        self.heart_rect.right, self.heart_rect.bottom = CARD_SIZE_W, CARD_SIZE_H
        self.image.blit(self.heart, self.heart_rect)

        self.text_hp = font.render(str(hp), True, self.hp_color)
        self.hp_rect = self.text_hp.get_rect()
        self.hp_rect.center = self.heart_rect.center[0], self.heart_rect.center[1] + 4
        self.image.blit(self.text_hp, self.hp_rect)

    # отрисовка урона
    def draw_damage(self, damage):
        self.damage = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, 'dp.png')),
                                            (CARD_SIZE_W / 4, CARD_SIZE_W / 4))
        self.damage_rect = self.heart.get_rect()
        self.damage_rect.left, self.damage_rect.bottom = 0, CARD_SIZE_H
        self.image.blit(self.damage, self.damage_rect)

        self.text_dp = font.render(str(self.dp), True, COLORS['WHITE'])
        self.dp_rect = self.text_dp.get_rect()
        self.dp_rect.center = self.damage_rect.center
        self.image.blit(self.text_dp, self.dp_rect)

    # отрисовка стоимости
    def draw_cost(self, cost):
        self.text_cost = font.render(str(self.cost), True, COLORS['WHITE'])
        self.cost_rect = self.text_cost.get_rect()
        self.cost_rect.center = CARD_SIZE_W - self.move_x, self.move_y + 2
        self.image.blit(self.text_cost, self.cost_rect)

    # отрисовка типа
    def draw_kind(self, kind):
        # 1 - floppa, 2 = robert
        self.text_kind = font.render(str(self.kind), True, CARD_TYPES[self.kind])
        self.kind_rect = self.text_kind.get_rect()
        self.kind_rect.center = self.move_x, self.move_y + 2
        self.image.blit(self.text_kind, self.kind_rect)

    def get_dp(self):
        return self.dp

    def get_hp(self):
        return self.hp

    # нанести урон карте
    def get_hit(self, damage):
        self.hp -= damage
        if damage != 0:
            self.hp_color = COLORS['RED']

    def update(self, *args, **kwargs) -> None:
        self.draw_hp(self.hp)
