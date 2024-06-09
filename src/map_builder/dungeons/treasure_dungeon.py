from .dungeon_type import DungeonType

class TreasureDungeon:
    def __init__(self) -> None:
        self.type = DungeonType.TREASURE.value

    def build(self) -> None:
        pass

    def get_type(self) -> str:
        return self.type