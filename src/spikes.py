import pygame
from const import *

class Spikes(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('graphics/spike.png')
        self.image = pygame.transform.scale(img, (tile_size, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#create spikes sprite group
spike_group = pygame.sprite.Group()