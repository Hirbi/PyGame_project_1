import os

WIDTH = 1600
HEIGHT = 900
FPS = 240
COLORS = {'BLACK': (0, 0, 0), "WHITE": (255, 255, 255), 'RED': (255, 0, 0), 'BLUE': (0, 255, 0), 'GREEN': (0, 0, 255)}


# путь к файлу
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'data', 'img')
player_folder = os.path.join(img_folder, 'player')