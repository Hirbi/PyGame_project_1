import pygame.sprite
from card import Card
from constants import all_sprites, COLORS, CARD_SIZE_W, CARD_SIZE_H


class CardPlace(pygame.sprite.Sprite):
    width, height = CARD_SIZE_W + 4, CARD_SIZE_H + 4

    def __init__(self, x=0, y=0, can_put=False, can_take=False):
        self.can_put, self.can_take = can_put, can_take
        pygame.sprite.Sprite.__init__(self)
        # устанавливаем поверхность
        self.image = pygame.Surface((CardPlace.width, CardPlace.height))
        self.image.set_colorkey((0, 0, 0))
        # рисуем прямоугольник
        pygame.draw.rect(self.image, COLORS['GREY'], pygame.Rect((0, 0), (CardPlace.width, CardPlace.height)), 2)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.card = None

    # возвращает карту к месту карты
    def move_back(self):
        if self.card is not None:
            self.card.set_cords(self.rect.left + 2, self.rect.top + 2)

    # установить карту на новое место
    def set_card(self, card):
        if self.card is not None:
            self.card.image = pygame.Surface((0, 0))
            all_sprites.remove(self.card)
        # устанавливаем карту
        self.card = card
        all_sprites.add(card)
        self.move_back()

    # очистка карты
    def delete_card(self):
        self.card = None

    # передвинуть карты
    def move_card(self, add_x, add_y):
        if self.card is not None and self.can_take:
            self.card.move_card(add_x, add_y)

    def is_in(self, x, y):
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def can_take_card(self, x, y):
        return self.is_in(x, y) and self.card is not None and self.can_take

    def can_put_card(self, x, y):
        return self.can_put and self.is_in(x, y)

    def set_card_cords(self, add_x, add_y):
        if self.card is not None:
            self.card.set_cords(add_x, add_y)

    def card_for_all(self):
        if self.card is not None:
            return self.card.all_tables
        return False

    def set_cords(self, x, y):
        self.rect.center = x, y

    def update(self) -> None:
        if self.card is not None and self.card.get_hp() <= 0:
            self.card.image = pygame.Surface((0, 0))
            all_sprites.remove(self.card)