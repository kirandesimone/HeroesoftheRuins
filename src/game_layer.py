from enum import Enum

class GameLayer(Enum):
    ALL_SPRITES = 0
    GROUND = 1
    WALL = 2
    ENEMY = 3
    PLAYER = 4