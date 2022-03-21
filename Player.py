import pygame
import os
import random
from constants import COLORS, WIDTH, HEIGHT, player_folder, CARD_SIZE_H, CARD_SIZE_W, all_sprites,\
    table_count, hand_count
from Card_place import CardPlace
from mob_card import MobCard


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, p_img="p1_jump.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, p_img)), (300, 300))
        self.rect = self.image.get_rect()
        self.hand = []
        self.table = []
        self.mana = 0
        self.hp = 30
        self.rect.left, self.rect.bottom = WIDTH, HEIGHT

    def your_turn(self):
        for i in range(len(self.table)):
            self.table[i].set_cords(
                WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.table) - 1)) + (CARD_SIZE_W + 4) * (i + 1.5),
                HEIGHT / 2 + (CARD_SIZE_H + 4) * 0.5)
            self.table[i].move_back()
        self.rect.right, self.rect.bottom = WIDTH, HEIGHT
        for i in range(len(self.hand)):
            self.hand[i].set_cords(WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.hand) - 1))
                                   + (CARD_SIZE_W + 4) * (i + 1.5),
                                   HEIGHT - (CARD_SIZE_H + 4) * 0.5)
            self.hand[i].move_back()
        all_sprites.update()

    def enemy_turn(self):
        for i in range(len(self.table)):
            self.table[i].set_cords(
                WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.table) - 1)) + (CARD_SIZE_W + 4) * (i + 1.5),
                HEIGHT / 2 - (CARD_SIZE_H + 4) * 0.5)
            self.table[i].move_back()
        self.rect.right, self.rect.top = WIDTH, 0
        for i in range(len(self.hand)):
            self.hand[i].set_cords(-100, -100)
            self.hand[i].move_back()
        all_sprites.update()

    def get_cards(self, *card_list):
        self.hand.extend(card_list)

    def start_game(self):
        for i in range(table_count):
            self.table.append(CardPlace(can_take=False, can_put=True))
        for i in range(hand_count):
            self.hand.append(CardPlace(can_take=True, can_put=False))
            self.hand[i].set_card(MobCard(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
                                              random.randint(1, 4)))

    def update(self):
        # self.move()
        pass

    def new_turn(self):
        self.mana = (self.mana + 1) % 10


