import pygame
from constants import COLORS, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, p_w=50, p_h=50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((p_w, p_h))
        self.image.fill(COLORS['GREEN'])
        self.rect = self.image.get_rect()
        self.rect.center = x + p_w / 2, y + p_h / 2

    def move(self, add_x=5, add_y=5):
        if 0 <= self.rect.x + add_x <= WIDTH - self.rect.width + 1:
            self.rect.x += add_x
        if 0 <= self.rect.y + add_y <= HEIGHT - self.rect.height + 1:
            self.rect.y += add_y

    def update(self):
        self.move()


