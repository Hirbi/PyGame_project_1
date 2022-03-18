import pygame
import random
from Player import Player
import os
from card import Card
from Card_place import CardPlace

# глобальные переменные
from constants import COLORS, WIDTH, HEIGHT, FPS, game_folder, img_folder, player_folder, all_sprites

# инициализация
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First try')
clock = pygame.time.Clock()
player = Player()
all_sprites.add(player)


def main():
    running = True
    mouse_down = False
    mouse_x, mouse_y = 0, 0
    card_count = 4
    cards_places = []
    for i in range(card_count):
        box = CardPlace(WIDTH / 2 - CardPlace.width * 2 + CardPlace.width * (i + 1.5), 500)
        new_card = Card(box.image)
        box.set_card(new_card)
        cards_places.append(box)
        # all_sprites.add(new_card)
    all_sprites.add(*cards_places)

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
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    for card_place in cards_places:
                        if card_place.is_in(*event.pos):
                            card_place.set_card_cords(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
                    mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
        # обновление
        all_sprites.update()

        # отрисовка
        screen.fill(COLORS['BLACK'])
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
