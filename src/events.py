from dataclasses import dataclass
from pygame import sprite

@dataclass
class Message():
    pass

@dataclass
class MoveMessage(Message):
    entity: sprite.Sprite
    x_position: int
    y_position: int

@dataclass
class AttackMessage(Message):
    attacker: sprite.Sprite
    target: sprite.Sprite

@dataclass
class CollideMessage(Message):
    confronter: sprite.Sprite
    blocker: sprite.Sprite

@dataclass
class EncounterMessage(Message):
    pass
