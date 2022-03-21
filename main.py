import pygame

pygame.init()

import random
from Player import Player
import os
from card import Card
from mob_card import MobCard
from Card_place import CardPlace

# глобальные переменные
from constants import COLORS, WIDTH, HEIGHT, FPS, game_folder, img_folder, player_folder, all_sprites

# инициализация
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('First try')
clock = pygame.time.Clock()
player_1 = Player()
player_2 = Player()
all_sprites.add(player_1, player_2)
background = pygame.image.load(os.path.join(img_folder, 'fon.jpg')).convert()
screen.blit(background, (0, 0))
pygame.display.update()


def game(now_player, other_player):
    now_player.your_turn()
    other_player.enemy_turn()
    # игрок 1
    for i in range(len(now_player.table)):
        now_player.table[i].set_cords(
            WIDTH / 2 - (CardPlace.width * (len(now_player.table) - 1)) + CardPlace.width * (i + 1.5),
            HEIGHT / 2 + CardPlace.height * 0.5)
        now_player.table[i].move_back()
    # игрок 2
    for i in range(len(other_player.table)):
        other_player.table[i].set_cords(
            WIDTH / 2 - (CardPlace.width * (len(other_player.table) - 1)) + CardPlace.width * (i + 1.5),
            HEIGHT / 2 - CardPlace.height * 0.5)
        other_player.table[i].move_back()
    all_sprites.update()

    screen.blit(background, (0, 0))
    running = True
    mouse_down = False
    mouse_x, mouse_y = 0, 0
    card_picked_num = None
    while running:
        # screen.blit(background, (0, 0))
        clock.tick(FPS)
        # в pygame.event.get() находятся все события pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    return
                mouse_x, mouse_y = event.pos
                mouse_down = True
                for i in range(len(now_player.table)):
                    if now_player.table[i].can_take_card(*event.pos):
                        card_picked_num = i
            if event.type == pygame.MOUSEMOTION:
                mouse_down = False
                if card_picked_num is not None:
                    now_player.table[card_picked_num].move_card(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
                    mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                print(mouse_down)
                if card_picked_num is not None:
                    table = now_player.table.copy()
                    if now_player.table[card_picked_num].card_for_all():
                        table += other_player.table
                    for i in range(len(table)):
                        if i != card_picked_num and table[i].can_put_card(*event.pos):
                            print(True)
                            table[i].set_card(now_player.table[card_picked_num].card)
                            table[card_picked_num].delete_card()
                            all_sprites.update()
                    all_sprites.update()
                card_picked_num = None
                for card_place in now_player.table:
                    card_place.move_back()
        # обновление
        pygame.display.flip()
        all_sprites.update()
        # отрисовка
        # screen.fill(COLORS['BLACK'])
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()


def main():
    card_count = 8
    for i in range(card_count // 2):
        player_1.table.append(CardPlace(can_take=True, can_put=True))
    for i in range(card_count // 2):
        player_2.table.append((CardPlace(can_take=True, can_put=True)))
    all_sprites.add(*player_1.table)
    all_sprites.add(*player_2.table)
    player_1.table[0].set_card(MobCard(10, 7, 4, 1, all_tables=True))
    player_1.table[1].set_card(MobCard(7, 4, 9, 3, mob_img='huy.png'))
    while True:
        game(player_1, player_2)
        game(player_2, player_1)


if __name__ == '__main__':
    main()
