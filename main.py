import pygame
import random
from Player import Player
import os
from card import Card

# глобальные переменные
from constants import COLORS, WIDTH, HEIGHT, FPS, game_folder, img_folder, player_folder

# инициализация
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First try')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


def main():
    running = True
    mouse_down = False
    mouse_x, mouse_y = 0, 0
    card_count = 4
    cards = []
    for i in range(card_count):
        box = Card((i + 1) * 50, 50)
        cards.append(box)
    print(cards)
    all_sprites.add(*cards)
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
                print(event.pos)
               # print(card_1.is_in(*event.pos))
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    for card in cards:
                        if card.is_in(*event.pos):
                            card.set_coords(event.pos[0] - mouse_x, event.pos[1] - mouse_y)
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
