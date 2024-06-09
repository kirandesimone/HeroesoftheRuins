from .dungeon_type import DungeonType

class EntranceDungeon:
    def __init__(self) -> None:
        self.type = DungeonType.ENTRANCE.value

    def build(self) -> None:
        pass

    def get_type(self) -> str:
        return self.type
        