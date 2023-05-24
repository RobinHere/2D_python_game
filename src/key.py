import pygame
from const import *

#create key sprite, load image, add rectangle
class Key(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('graphics/key.png')
        self.image = pygame.transform.scale(img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#create key sprite group
key_group = pygame.sprite.Group()