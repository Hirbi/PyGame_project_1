import pygame
import random
from Player import Player
import os

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
    while running:
        clock.tick(FPS)
        # в pygame.event.get() находятся все события pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
        # обновление
        all_sprites.update()

        # отрисовка
        screen.fill(COLORS['BLACK'])
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
