import os
import pygame

WIDTH = 1600
HEIGHT = 900
FPS = 240
COLORS = {'BLACK': (0, 0, 0), "WHITE": (255, 255, 255), 'RED': (255, 0, 0), 'BLUE': (0, 255, 0), 'GREEN': (0, 0, 255),
          "GREY": (155, 155, 155)}


all_sprites = pygame.sprite.Group()

# путь к файлу
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'data', 'img')
player_folder = os.path.join(img_folder, 'player')