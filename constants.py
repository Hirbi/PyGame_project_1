import os
import pygame

WIDTH = 1920
HEIGHT = 1050
FPS = 240
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
font = pygame.font.Font(None, 30)

CARD_SIZE_W, CARD_SIZE_H = 150, 225
COLORS = {'BLACK': (0, 0, 0), "WHITE": (255, 255, 255), 'RED': (255, 0, 0), 'BLUE': (0, 0, 255), 'GREEN': (0, 255, 0),
          "GREY": (155, 155, 155), "YELLOW": (255, 255, 0)}

CARD_TYPES = {0: COLORS["BLACK"], 1: COLORS['BLUE'], 2: COLORS['RED'], 3: COLORS['GREEN'], 4: COLORS['YELLOW']}


all_sprites = pygame.sprite.Group()

# путь к файлу
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'data', 'img')
player_folder = os.path.join(img_folder, 'player')

# для игры
table_count = 4
hand_count = 4
# шрифт
# print(pygame.font.get_fonts())
