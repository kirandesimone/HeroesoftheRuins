import pygame

from typing import Any

from ..game_layer import GameLayer
from ..events import *

PLAYER_HEIGHT = 32
PLAYER_WIDTH = 32
PLAYER_SPEED = 3
STARTING_X_POS = 1
STARTING_Y_POS = 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, *groups):
        self._layer = GameLayer.PLAYER.value
        pygame.sprite.Sprite.__init__(self, groups) # type: ignore

        self.x_position = x_position * PLAYER_WIDTH
        self.y_position = y_position * PLAYER_HEIGHT
        self.height = PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.facing = "down"
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    def move(self, direction: str):
        match direction:
            case "up":
                self.rect.y -= PLAYER_SPEED
                self.facing = "up"
            case "down":
                self.rect.y += PLAYER_SPEED
                self.facing = "down"
            case "left":
                self.rect.x -= PLAYER_SPEED
                self.facing = "left"
            case "right":
                self.rect.x += PLAYER_SPEED
                self.facing = "right"
                
   
    def update(self, *args: Any, **kwargs: Any) -> None:
        if len(args) == 0:
            return
        
        messages: list[Message] = args[0]

        for message in messages:
            print(message)
            if isinstance(message, MoveMessage) and message.entity is self:
                self.move(message.direction)
            else:
                pass
    