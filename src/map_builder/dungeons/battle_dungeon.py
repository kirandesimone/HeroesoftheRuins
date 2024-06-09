from .dungeon_type import DungeonType


class BattleDungeon:
    def __init__(self) -> None:
        self.type = DungeonType.BATTLE.value
    
    def build(self) -> None:
        pass

    def get_type(self) -> str:
        return self.type