import pygame

from typing import Any, List
from ..game_layer import GameLayer
from ..events import *

PLAYER_HEIGHT = 32
PLAYER_WIDTH = 32
STARTING_X_POS = 1
STARTING_Y_POS = 1

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = GameLayer.PLAYER.value
        pygame.sprite.Sprite.__init__(self, groups)

        self.x_position = STARTING_X_POS * PLAYER_WIDTH
        self.y_position = STARTING_Y_POS * PLAYER_HEIGHT
        self.height = PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    def move(self, x_position, y_position):
        self.rect.x += x_position
        self.rect.y += y_position
   
    def update(self, *args: Any, **kwargs: Any) -> None:
        if len(args) == 0:
            return
        
        messages: List[Message] = args[0]

        for message in messages:
            if isinstance(message, MoveMessage):
                self.move(message.x_position, message.y_position)
            elif isinstance(message, AttackMessage):
                pass
            else:
                pass
    