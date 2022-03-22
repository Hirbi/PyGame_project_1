import pygame
import os
import random
from constants import COLORS, WIDTH, HEIGHT, player_folder, CARD_SIZE_H, CARD_SIZE_W, all_sprites,\
    table_count, hand_count, font, screen
from Card_place import CardPlace
from mob_card import MobCard


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, p_img="p1_jump.png"):
        self.hp = 30

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, p_img)), (300, 300))
        self.rect = self.image.get_rect()
        self.hand = []
        self.table = []
        self.mana = 0
        self.hp = 30
        self.text_hp = font.render(str(self.hp), True, COLORS['WHITE'])
        self.hp_rect = self.text_hp.get_rect()

    def your_turn(self):
        for i in range(len(self.table)):
            self.table[i].set_cords(
                WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.table) - 1)) + (CARD_SIZE_W + 4) * (i + 1.5),
                HEIGHT / 2 + (CARD_SIZE_H + 4) * 0.5)
            self.table[i].move_back()
        self.rect.left, self.rect.bottom = 0, HEIGHT
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
        self.rect.left, self.rect.top = 0, 0
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
        print(True, ' player class')
        self.text_hp = font.render(str(self.hp), True, COLORS['WHITE'])
        self.hp_rect = self.text_hp.get_rect()
        self.hp_rect.right, self.hp_rect.bottom = WIDTH, HEIGHT
        screen.blit(self.text_hp, self.hp_rect)

    def new_turn(self):
        self.mana = (self.mana + 1) % 10

    def delete_card(self, card_picked_num):
        self.hand[card_picked_num].delete_it()
        self.hand.remove(self.hand[card_picked_num])

    # разыгрывание карты с руки
    def replace_card(self, card_picked_num, other_player, pos):
        if card_picked_num is not None:
            table = self.table.copy()
            if self.hand[card_picked_num].card_for_all():
                table += other_player.table
            for i in range(len(table)):
                if table[i].can_put_card(*pos):
                    table[i].set_card(self.hand[card_picked_num].card)
                    self.delete_card(card_picked_num)

    # вывод номера карты, которую можно взять
    def can_take_card(self, pos):
        for i in range(len(self.hand)):
            if self.hand[i].can_take_card(*pos):
                return i