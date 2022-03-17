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
            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    player.move(0, -5)
                elif event.key == 97:
                    player.move(-5, 0)
                elif event.key == 115:
                    player.move(0, 5)
                elif event.key == 100:
                    player.move(5, 0)

                print(event.key)
        # обновление
        all_sprites.update()

        # отрисовка
        screen.fill(COLORS['BLUE'])
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
