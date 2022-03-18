import pygame.sprite
from card import Card
from constants import all_sprites, COLORS, WIDTH, HEIGHT


class CardPlace(pygame.sprite.Sprite):
    width = 105 # x
    height = 155 # y

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        # устанавливаем поверхность
        self.image = pygame.Surface((CardPlace.width, CardPlace.height))
        # рисуем прямоугольник
        pygame.draw.rect(self.image, COLORS['GREY'], pygame.Rect((0, 0), (CardPlace.width, CardPlace.height)), 2)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.card = None

    def set_card(self, card):
        # устанавливаем карту
        card.set_surface(self.image)
        self.card = card
        all_sprites.add(card)

    def is_in(self, x, y):
        if self.card is not None:
            return self.card.is_in(x, y)
        return False

    def set_card_cords(self, add_x, add_y):
        if self.card is not None:
            self.card.set_cords(add_x, add_y)


