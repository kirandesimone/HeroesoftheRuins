import pygame

from ..game_layer import GameLayer


GREEN = (0, 255, 0)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, tilesize, *groups) -> None:
        self._layer = GameLayer.WALL.value
        pygame.sprite.Sprite.__init__(self, groups)

        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x_position * tilesize
        self.rect.y = y_position * tilesize