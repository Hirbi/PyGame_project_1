import pygame

from constants import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, w=100, h=100, img="not_found_img.png", text="no_text", text_color=COLORS['WHITE']):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, img)),
                                            (w, h))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        if text != "":
            self.text = pygame.transform.scale(font.render(text, True, text_color), (w * 0.8, h * 0.6))
            self.text_rect = self.text.get_rect()
            self.text_rect.center = self.rect.width / 2, self.rect.height / 2
            self.image.blit(self.text, self.text_rect)

    def is_in(self, x, y):
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def set_cords(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs) -> None:
        pass
