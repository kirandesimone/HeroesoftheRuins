import pygame
from ..game_layer import GameLayer

BLUE = (0, 0, 255)

class Floor(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, tilesize, *groups) -> None:
        self._layer = GameLayer.FLOOR.value
        pygame.sprite.Sprite.__init__(self, groups)

        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_position * tilesize
        self.rect.y = y_position * tilesize

