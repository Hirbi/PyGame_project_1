import pygame
import random

# глобальные переменные
WIDTH = 360
HEIGHT = 480
FPS = 30
COLORS = {'BLACK': (0, 0, 0), "WHITE": (255, 255, 255), 'RED': (255, 0, 0), 'BLUE': (0, 255, 0), 'GREEN': (0, 0, 255)}

# инициализация
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First try')
clock = pygame.time.Clock()


def main():
    running = True
    while running:
        screen.fill(COLORS['BLACK'])
        pygame.display.flip()

if __name__ == '__main__':
    main()
