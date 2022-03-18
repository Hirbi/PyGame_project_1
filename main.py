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
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First try')
clock = pygame.time.Clock()
player = Player()
all_sprites.add(player)
print(len(all_sprites))


def main():
    running = True
    mouse_down = False
    mouse_x, mouse_y = 0, 0
    card_count = 8
    cards_places = []
    for i in range(card_count // 2):
        cards_places.append(CardPlace(WIDTH / 2 - CardPlace.width * 2 + CardPlace.width * (i + 1.5), 500))
    for i in range(card_count // 2):
        cards_places.append((CardPlace(WIDTH / 2 - CardPlace.width * 2 + CardPlace.width * (i + 1.5), 275)))
    all_sprites.add(*cards_places)
    cards_places[0].set_card(MobCard(10, 7))
    cards_places[1].set_card(MobCard(9, 12))

    card_picked_num = None
    while running:
        clock.tick(FPS)
        # в pygame.event.get() находятся все события pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse_down = True
                for i in range(len(cards_places)):
                    if cards_places[i].is_in(*event.pos) and cards_places[i].card is not None:
                        card_picked_num = i
            if event.type == pygame.MOUSEMOTION:
                if card_picked_num is not None:
                    cards_places[card_picked_num].move_card(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
                    mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                print(card_picked_num)
                mouse_down = False
                if card_picked_num is not None:
                    for i in range(len(cards_places)):
                        if i != card_picked_num and cards_places[i].is_in(*event.pos):
                            print(i)
                            cards_places[i].set_card(cards_places[card_picked_num].card)
                            cards_places[card_picked_num].delete_card()
                            print(i)
                            all_sprites.update()
                card_picked_num = None
                for card_place in cards_places:
                    card_place.move_back()
        # обновление
        all_sprites.update()

        # отрисовка
        screen.fill(COLORS['BLACK'])
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
