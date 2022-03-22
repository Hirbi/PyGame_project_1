import pygame

pygame.init()

import random
from Player import Player
import os
from card import Card
from mob_card import MobCard
from Card_place import CardPlace

# глобальные переменные
from constants import screen, WIDTH, HEIGHT, FPS, game_folder, img_folder, player_folder,\
    all_sprites, table_count, hand_count

# инициализация
pygame.display.set_caption('First try')
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join(img_folder, 'fon.jpg'))
screen.blit(background, (0, 0))
pygame.display.update()


def game(now_player, other_player):
    now_player.your_turn()
    other_player.enemy_turn()
    all_sprites.update()

    screen.blit(background, (0, 0))
    running = True
    mouse_down = False
    mouse_x, mouse_y = 0, 0
    card_picked_num = None
    while running:
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
                card_picked_num = now_player.can_take_card(event.pos)
            if event.type == pygame.MOUSEMOTION:
                mouse_down = False
                if card_picked_num is not None:
                    now_player.hand[card_picked_num].move_card(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
                    mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                now_player.replace_card(card_picked_num, other_player, event.pos)
                all_sprites.update()
                card_picked_num = None
                for card_place in now_player.hand:
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
    player_1 = Player(p_img='floppa.png')
    player_2 = Player(p_img='robert.png')
    all_sprites.add(player_1, player_2)
    player_1.start_game()
    player_2.start_game()
    all_sprites.add(*player_1.table, *player_1.hand)
    all_sprites.add(*player_2.table, *player_2.hand)
    while True:
        game(player_1, player_2)
        game(player_2, player_1)


if __name__ == '__main__':
    main()
