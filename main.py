import pygame

pygame.init()

import random
from Player import Player
import os
from card import Card
from mob_card import MobCard
from Card_place import CardPlace
from mana import Mana

# глобальные переменные
from constants import screen, WIDTH, HEIGHT, FPS, game_folder, img_folder, player_folder, \
    all_sprites, table_count, hand_count

# инициализация
pygame.display.set_caption('Card game')
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'background.jpg')), (WIDTH, HEIGHT))
# background = pygame.image.load(os.path.join(img_folder, 'try.jpg'))
screen.blit(background, (0, 0))
pygame.display.update()
pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


def game(now_player, other_player):
    crystal = Mana(1655, 670)
    all_sprites.add(crystal)
    now_player.turn(True)
    other_player.turn(False)
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
            if event.type == pygame.KEYDOWN:
                # print(event.key)
                if event.key == 13: # Enter
                    now_player.end_turn(other_player)
                    return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.button)
                mouse_x, mouse_y = event.pos
                mouse_down = True
                card_picked_num = now_player.can_take_card(event.pos)
            if event.type == pygame.MOUSEMOTION:
                mouse_down = False
                if card_picked_num is not None:
                    now_player.hand[card_picked_num].move_card(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
                    mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if card_picked_num is not None:
                    now_player.play_card(card_picked_num, other_player, event.pos)
                    now_player.move_cards_back()
                    card_picked_num = None
                else:
                    now_player.activate_card(event.pos, event.button)
        # отрисовка
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()


def main():
    player_1 = Player(1, p_img='floppa.png')
    player_2 = Player(2, p_img='robert.png')
    all_sprites.add(player_1, player_2)
    player_1.start_game()
    player_2.start_game()
    all_sprites.add(*player_1.table, *player_1.hand)
    all_sprites.add(*player_2.table, *player_2.hand)
    while True:
        game(player_1, player_2)
        player_1.new_turn()
        game(player_2, player_1)
        player_2.new_turn()


if __name__ == '__main__':
    main()
