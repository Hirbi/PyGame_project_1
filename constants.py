import os
import random
from random import randint
import pygame

WIDTH, HEIGHT = 1900, 1080
CARD_SIZE_W, CARD_SIZE_H = 150, 225
P_WIDTH, P_HEIGHT = 250, 250
FPS = 240
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
font = pygame.font.Font(None, 30)
player_font = pygame.font.Font(None, 60)

COLORS = {'BLACK': (0, 0, 0), "WHITE": (255, 255, 255), 'RED': (255, 0, 0), 'BLUE': (0, 0, 255), 'GREEN': (0, 255, 0),
          "GREY": (155, 155, 155), "YELLOW": (255, 255, 0)}

CARD_TYPES = {0: COLORS["BLACK"], 1: COLORS['BLUE'], 2: COLORS['RED'], 3: COLORS['GREEN'], 4: COLORS['YELLOW']}
new_ = [(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 4)) for _ in range(30)]
floppa = [(5, 4, 4, 1), (3, 6, 2, 1), (1, 3, 3, 1), (7, 7, 5, 1), (10, 9, 10, 2), (6, 5, 9, 1), (3, 3, 6, 3),
          (10, 3, 8, 1), (6, 1, 6, 1), (6, 6, 1, 1), (5, 2, 7, 1), (1, 1, 10, 1), (9, 1, 7, 1), (2, 3, 6, 1),
          (4, 2, 6, 1), (10, 10, 2, 1), (3, 1, 5, 1), (9, 2, 6, 1), (7, 1, 1, 3), (9, 10, 2, 3), (7, 7, 2, 1),
          (2, 1, 9, 1), (8, 9, 10, 1), (1, 7, 7, 1), (7, 6, 8, 1), (2, 7, 1, 1), (3, 6, 3, 4), (2, 9, 7, 3),
          (3, 4, 1, 1), (9, 9, 4, 1)]
# random.shuffle(floppa)
robert = [(2, 2, 6, 2, 'coco-monke.png'), (5, 10, 5, 2, 'monkey_selfie.png'), (4, 7, 1, 2), (8, 3, 1, 2), (8, 7, 8, 2),
          (2, 1, 10, 2), (7, 9, 3, 2),
          (7, 1, 1, 2), (9, 10, 5, 2), (5, 4, 7, 2), (4, 4, 3, 2), (1, 6, 6, 2), (8, 9, 8, 2), (2, 1, 6, 2),
          (9, 9, 8, 2), (1, 2, 7, 2), (8, 10, 1, 2), (7, 1, 8, 2), (7, 10, 1, 2), (10, 8, 9, 2), (4, 10, 9, 2),
          (9, 10, 6, 2), (7, 7, 8, 2), (6, 5, 10, 2), (2, 5, 6, 2), (1, 10, 1, 2), (9, 1, 5, 2), (10, 4, 7, 2),
          (3, 7, 8, 2), (2, 6, 2, 2)]
# random.shuffle(robert)
all_decks = {1: floppa, 2: robert}

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
