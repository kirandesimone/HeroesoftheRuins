from dataclasses import dataclass
from pygame import sprite

@dataclass
class Message():
    pass

@dataclass
class MoveMessage(Message):
    entity: sprite.Sprite
    direction: str

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

@dataclass
class NextDungeon(Message):
    pass