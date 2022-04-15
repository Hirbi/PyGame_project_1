import pygame
import os
import random
from constants import COLORS, WIDTH, HEIGHT, player_folder, CARD_SIZE_H, CARD_SIZE_W, all_sprites, \
    table_count, hand_count, font, screen, all_decks, P_WIDTH, P_HEIGHT, player_font
from Card_place import CardPlace
from mob_card import MobCard
from mana import Mana


class Player(pygame.sprite.Sprite):
    def __init__(self, p_class, x=0, y=0, p_img="p1_jump.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, p_img)), (P_WIDTH, P_HEIGHT))
        self.rect = self.image.get_rect()
        self.hand = []
        self.deck = [MobCard(*stats) for stats in all_decks[p_class]]
        random.shuffle(self.deck)
        self.table = []
        self.mana = []
        self.hp = 30

        self.empty_deck_damage = 0
        # иконка сердца для персонажа
        self.heart = pygame.transform.scale(pygame.image.load(os.path.join(player_folder, 'hp.png')),
                                            (P_WIDTH // 3, P_HEIGHT // 3))
        self.heart_rect = self.heart.get_rect()
        self.heart_rect.right, self.heart_rect.bottom = P_WIDTH, P_HEIGHT

    # перемещение карт руки у игроков
    def move_hand(self, my_turn):
        if my_turn:
            for i in range(len(self.hand)):
                self.hand[i].set_cords(
                    WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.hand) - 1) // 2) + (CARD_SIZE_W + 4) * i,
                    HEIGHT - (CARD_SIZE_H + 4) * 0.5)
                self.hand[i].move_back()
        else:
            for i in range(len(self.hand)):
                self.hand[i].set_cords(-100, -100)
                self.hand[i].move_back()

    # перемещение стола
    def move_table(self, my_turn):
        for i in range(len(self.table)):
            self.table[i].set_cords(
                WIDTH / 2 - ((CARD_SIZE_W + 4) * (len(self.table) - 1) // 2) + (CARD_SIZE_W + 4) * i,
                HEIGHT / 2 + (CARD_SIZE_H + 4) * 0.5 * (1 if my_turn else -1))
            self.table[i].move_back()

    def turn(self, my_turn):
        self.move_table(my_turn)
        if my_turn:
            self.rect.left, self.rect.bottom = 0, HEIGHT
        else:
            self.rect.center = WIDTH // 2, P_HEIGHT // 2
        self.move_hand(my_turn)
        all_sprites.update()

    # получение карт через CardPlace
    def get_cards(self, *card_list):
        self.hand.extend(card_list)

    # начало игры
    def start_game(self):
        for i in range(table_count):
            self.table.append(CardPlace(can_put=True))
        for i in range(hand_count):
            self.hand.append(CardPlace(card=self.deck.pop(), can_take=True))

    # начало нового хода
    def new_turn(self):
        self.mana.append(Mana())
        if len(self.hand) <= 5 and len(self.deck) != 0:
            self.hand.append(CardPlace(card=self.deck.pop(), can_take=True, can_put=False))
        elif len(self.deck) != 0:
            self.deck.pop()
        elif len(self.deck) == 0:
            self.empty_deck_damage += 1
        self.hp -= self.empty_deck_damage

    def delete_card(self, card_picked_num):
        self.hand[card_picked_num].delete_it()
        self.hand.remove(self.hand[card_picked_num])
        self.move_hand(True)

    # разыгрывание карты с руки
    def play_card(self, card_picked_num, other_player, pos):
        if card_picked_num is not None:
            table = self.table.copy()
            # если карту можно положить на любой стол нужно добавить стол противника
            if self.hand[card_picked_num].card_for_all():
                table += other_player.table
            for i in range(len(table)):
                if table[i].can_put_card(*pos):
                    table[i].set_card(self.hand[card_picked_num].card)
                    self.delete_card(card_picked_num)

    # активация карт
    def activate_card(self, pos, button):
        table = self.table.copy()
        for i in range(len(table)):
            if table[i].can_interact_card(*pos):
                table[i].set_action(button)
        all_sprites.update()

    # нанести урон персонажу
    def get_hit(self, damage: int):
        self.hp -= damage

    # атака и использование способностей карт
    def end_turn(self, other_player):
        for i in range(len(self.table)):
            if other_player.table[i].is_empty() and self.table[i].can_attack():
                other_player.get_hit(self.table[i].attack())
            elif self.table[i].can_attack():
                other_player.table[i].get_hit(self.table[i].attack())
                self.table[i].get_hit(other_player.table[i].attack())
        all_sprites.update()

    # вывод номера карты, которую можно взять
    def can_take_card(self, pos):
        for i in range(len(self.hand)):
            if self.hand[i].can_take_card(*pos):
                return i
        return None

    # вернуть все карты обратно
    def move_cards_back(self):
        for card_place in self.hand:
            card_place.move_back()

    def update(self):
        self.image.blit(self.heart, self.heart_rect)
        self.text_hp = player_font.render(str(self.hp), True, COLORS["WHITE"] if self.hp == 30 else COLORS["RED"])
        self.hp_rect = self.text_hp.get_rect()
        self.hp_rect.center = self.heart_rect.center
        self.image.blit(self.text_hp, self.hp_rect)
